# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

__version__ = '0.0.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))

PORT = 5555


def root():
    current = os.path.dirname(__file__)
    current = os.path.join(current, '..')
    current = os.path.abspath(current)
    return current


def content():
    result = os.path.join(root(), 'content')
    assert os.path.exists(result), str(result)
    return result


def tmp():
    result = os.path.join(root(), '.tmp')
    return result


def build():
    result = os.path.join(tmp(), 'build')
    return result


def html():
    result = os.path.join(build(), 'index.html')
    return str(result)
