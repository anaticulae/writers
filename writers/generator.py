# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import webbrowser

import utila

import writers


def generate(show: bool = False, verbose: bool = True) -> int:
    tmp = writers.tmp()
    os.makedirs(tmp, exist_ok=True)

    source = writers.content()
    build = writers.build()
    os.makedirs(build, exist_ok=True)

    cmd = f'sphinx-build {source} {build} -j=auto'
    completed = utila.run(cmd)

    if completed.returncode:
        utila.log(completed.stdout)
        utila.log(completed.stderr)
        return completed.returncode

    if verbose:
        utila.log(completed.stdout)

    if show:
        html = writers.html()
        assert os.path.exists(html), html
        webbrowser.open(html)
    return utila.SUCCESS
