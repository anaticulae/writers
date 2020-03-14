# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import writers


def validate_reference(reference: str) -> bool:
    """Check that reference is defined in docs

    >>> validate_reference('elemente/inhaltsverzeichnis.html#abkuerzungen')
    True

    >>> validate_reference('aufbau_gliederung/index.html')
    True

    >>> validate_reference('index.html#notexists')
    Traceback (most recent call last):
        ...
    writers.verify.HashNotExists: notexists

    >>> validate_reference('filenotexists.html#abkuerzungen')
    Traceback (most recent call last):
        ...
    writers.verify.FileNotExists: ...html

    Args:
        reference(path): contains out of filepath.html#reference
    Raises:
        FileNotExists: path of reference does not exists
        HashNotExists: reference after # does not exists
    Returns:
        True if reference exists
    """
    source = writers.build()
    assert os.path.exists(source), str(source)

    try:
        _path, _ref = reference.split('#')
    except ValueError:
        _path, _ref = reference, ''

    path = os.path.join(source, _path)
    if not os.path.exists(path):
        raise FileNotExists(path)
    content = utila.file_read(path)
    if not _ref in content:
        raise HashNotExists(_ref)
    return True


class ReferenceException(ValueError):
    pass


class FileNotExists(ReferenceError):
    pass


class HashNotExists(ReferenceError):
    pass
