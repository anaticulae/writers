# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

from writers.generator import generate
from writers.verify import FileNotExists
from writers.verify import HashNotExists
from writers.verify import ReferenceException
from writers.verify import replace
from writers.verify import solve
from writers.verify import validate
from writers.verify import validate_template

__version__ = '1.0.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROCESS = 'writers'

PORT = 5555


def root():
    current = os.path.dirname(__file__)
    return current


def static():
    result = os.path.join(root(), '..', 'static')
    result = os.path.normpath(result)
    assert os.path.exists(result), str(result)
    return result


def build():
    result = os.path.join(root(), '..', 'build')
    result = os.path.normpath(result)
    return result


def html():
    result = os.path.join(build(), 'index.html')
    return str(result)
