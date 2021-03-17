# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila
import utilatest

import writers
import writers.generator


def install_requirements():
    utilatest.clean_install(os.path.join(writers.ROOT, '..'), writers.PROCESS)


def update_resources():
    if os.path.exists(writers.html()):
        return
    build = writers.build()
    os.makedirs(build, exist_ok=True)
    returncode = writers.generator.generate(path=build)
    assert returncode == utila.SUCCESS
