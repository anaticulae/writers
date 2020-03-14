# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import re

import utila

import writers


def validate(reference: str):
    """Check that reference is defined in docs

    >>> validate('elemente/inhaltsverzeichnis.html#abkuerzungen')
    >>> validate('aufbau_gliederung/index.html')

    >>> validate('index.html#notexists')
    Traceback (most recent call last):
        ...
    writers.verify.HashNotExists: #notexists

    >>> validate('filenotexists.html#abkuerzungen')
    Traceback (most recent call last):
        ...
    writers.verify.FileNotExists: ...html

    Args:
        reference(path): contains out of filepath.html#reference
    Raises:
        FileNotExists: path of reference does not exists
        HashNotExists: reference after # does not exists
    """
    source = writers.build()
    assert os.path.exists(source), str(source)

    reference = solve(reference)
    try:
        _path, _ref = reference.split('#')
        _ref = f'#{_ref}'
    except ValueError:
        _path, _ref = reference, ''

    path = os.path.join(source, _path)
    if not os.path.exists(path):
        raise FileNotExists(path)
    content = utila.file_read(path)
    if not _ref in content:
        raise HashNotExists(_ref)


def solve(reference: str):
    """Add path information to simple reference.

    >>> solve('elemente/deckblatt#zwingend-notwendige-angaben')
    'elemente/deckblatt.html#zwingend-notwendige-angaben'
    >>> solve('elemente/deckblatt')
    'elemente/deckblatt.html'
    >>> solve('elemente#helm')
    'elemente.html#helm'
    """
    if not '#' in reference and not '.html' in reference:
        return f'{reference}.html'
    if '.html' in reference:
        # no simple refrence
        return reference
    return reference.replace('#', '.html#')


URL_PATTERN = r'({(?P<link>[\w\-#/]+)}(?:\[(?P<description>\w+)\])?)'


def replace(content: str, url: str, template: callable = None) -> str:
    """Replace `{url}[content]?` pattern in `content` message.

    Pattern:
        {url}              -> <a href="checkitweg.de/url">weitere Informationen</a>
        {url}[description] -> <a href="checkitweg.de/url">[description]</a>

    >>> replace('Headline\\n{elemente/deckblatt#notwendige-angaben}[Message]',
    ... 'http://checkitweg.de/')
    'Headline\\n<a href="http://checkitweg.de/elemente/deckblatt.html#notwendige-angaben" target="_blank">Message</a>'

    >>> replace('Headline\\n{elemente/deckblatt#notwendige-angaben}',
    ... 'http://checkitweg.de/')
    'Headline\\n<a href="http://checkitweg.de/elemente/deckblatt.html#notwendige-angaben" target="_blank">weitere Informationen</a>'
    """
    assert url.endswith('/'), url
    if not template:
        template = link_processor
    assert callable(template), type(template)
    for item in re.findall(URL_PATTERN, content):
        pattern, link, description = item
        if not description:
            description = 'weitere Informationen'
        new_url = url + solve(link)
        href = link_processor(url=new_url, description=description)
        content = content.replace(pattern, href, 1)
    return content


def validate_template(content: str):
    """Extract list of invalid links.

    >>> validate_template('{elemente/deckblatt#notwendige-angaben}[Message]}')
    [('{elemente/deckblatt#notwendige-angaben}[Message]', 'elemente/deckblatt.html#notwendige-angaben')]
    >>> validate_template('No links in content can not have invalid links')
    []
    """
    invalid = []
    for item in re.findall(URL_PATTERN, content):
        matched, link, _ = item
        solved = solve(link)
        try:
            validate(solved)
        except ReferenceException:
            invalid.append((matched, solved))
    return invalid


def link_processor(url, description):
    return f'<a href="{url}" target="_blank">{description}</a>'


class ReferenceException(ValueError):
    pass


class FileNotExists(ReferenceException):
    pass


class HashNotExists(ReferenceException):
    pass
