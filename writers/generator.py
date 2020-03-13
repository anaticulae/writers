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


def generate(
        path: str = None,
        show: bool = False,
        verbose: bool = False,
) -> int:
    """Use Sphinx to generate documentation. If `path` is None the
    default doc output location is used, if not path must exists and the
    generator will put the generated files there.

    Args:
        path(str): path to write results
        show(bool): if True open in webbrowser after generation
        verbose(bool): describe what is beeing done
    Returns:
        Returncode of Sphinx generation process.
    """
    utila.call('generate docs')
    assert path is None or os.path.exists(path), str(path)

    if path is None:
        tmp = writers.tmp()
        os.makedirs(tmp, exist_ok=True)

    source = writers.content()

    build = writers.build() if path is None else path
    if path is None:
        os.makedirs(build, exist_ok=True)

    cmd = f'sphinx-build {source} {build} -j=auto -n -v -W --keep-going'
    completed = utila.run(cmd)

    if completed.returncode:
        utila.info(completed.stdout)
        utila.error(completed.stderr)
        return completed.returncode

    if verbose:
        utila.log(completed.stdout)

    if show:
        html = writers.html()
        if path is None:
            html = os.path.join(path, 'index.html')
        assert os.path.exists(html), html
        webbrowser.open(html)
    return utila.SUCCESS
