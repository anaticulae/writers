# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import writers


def validate(reference: str):
    """Check that reference is defined in docs.

    >>> validate('elemente/inhaltsverzeichnis.html#abkurzungen')
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
    assert os.path.exists(source), f'{source} run `writers --build`'
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
    if _ref not in content:
        raise HashNotExists(_ref)


def solve(reference: str):
    """Add path information to simple reference.

    >>> solve('elemente/titelblatt#zwingend-notwendige-angaben')
    'elemente/titelblatt.html#zwingend-notwendige-angaben'
    >>> solve('elemente/titelblatt')
    'elemente/titelblatt.html'
    >>> solve('elemente#helm')
    'elemente.html#helm'
    """
    if '#' not in reference and '.html' not in reference:
        return f'{reference}.html'
    if '.html' in reference:
        # no simple refrence
        return reference
    return reference.replace('#', '.html#')


URL_PATTERN = utila.compiles(r"""
    (
        {(?P<link>[\w\-\.#/]+)}             # support .html and #anker in links
        (?:\[(?P<description>\w+)\])?       # optional description
    )
""")


def replace(content: str, url: str, template: callable = None) -> str:
    """Replace `{url}[content]?` pattern in `content` message.

    Pattern:
        {url}              -> <a href="checkitweg.de/url">weitere Informationen</a>
        {url}[description] -> <a href="checkitweg.de/url">[description]</a>

    >>> replace('Headline\\n{elemente/titelblatt#notwendige-angaben}[Message]',
    ... 'http://checkitweg.de/')
    'Headline\\n<a href="http://checkitweg.de/elemente/titelblatt.html#notwendige-angaben" target="_blank">Message</a>'

    >>> replace('Headline\\n{elemente/titelblatt#notwendige-angaben}',
    ... 'http://checkitweg.de/')
    'Headline\\n<a href="http://checkitweg.de/elemente/titelblatt.html#notwendige-angaben" target="_blank">weitere Informationen</a>'
    """
    assert url.endswith('/'), url
    if not template:
        template = link_processor
    assert callable(template), type(template)
    for item in URL_PATTERN.findall(content):
        pattern, link, description = item
        if not description:
            description = 'weitere Informationen'
        new_url = url + solve(link)
        href = link_processor(url=new_url, description=description)
        content = content.replace(pattern, href, 1)
    return content


def validate_template(content: str):
    """Extract list of invalid links.

    >>> validate_template('{elemente/titelblatt#notwendige-angaben}[Message]}')
    [('{elemente/titelblatt#notwendige-angaben}[Message]', 'elemente/titelblatt.html#notwendige-angaben')]
    >>> validate_template('No links in content can not have invalid links')
    []
    >>> validate_template('{elemente/error_with_html.html#titelblatt}')
    [('{elemente/error_with_html.html#titelblatt}', 'elemente/error_with_html.html#titelblatt')]
    >>> validate_template('{{jinja_value}}')
    []
    """
    # do not detect jinja-value as broken reference
    content = content.replace('{{', '**')  # TODO: TO STUPID TO FIX REGEX
    invalid = []
    for item in URL_PATTERN.findall(content):
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
