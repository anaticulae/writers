# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
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
        dirty: bool = False,
        verbose: bool = False,
) -> int:
    """Use Sphinx to generate documentation. If `path` is None the
    default doc output location is used, if not path must exists and the
    generator will put the generated files there.

    Args:
        path(str): path to write results
        show(bool): if True open in webbrowser after generation
        dirty(bool): ignore warnings and errors
        verbose(bool): describe what is beeing done
    Returns:
        Returncode of Sphinx generation process.
    """
    utila.log('generate docs')
    assert path is None or os.path.exists(path), str(path)

    source = writers.static()

    build = writers.build() if path is None else path
    if path is None:
        os.makedirs(build, exist_ok=True)

    warnings_as_errors = '-W --keep-going' if not dirty else ''
    cmd = f'sphinx-build {source} {build} -j=auto -n -v {warnings_as_errors}'
    if verbose:
        utila.log(cmd)
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


def open_generated():
    html = writers.html()
    webbrowser.open(html)
    return utila.SUCCESS
