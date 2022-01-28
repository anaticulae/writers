# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import webbrowser

import pytest
import utilatest

import writers.generator


@utilatest.skip_longrun
@pytest.mark.parametrize('show', [True, False])
def test_generator_generate(show, testdir, monkeypatch):
    root = testdir.tmpdir

    with monkeypatch.context() as context:
        context.setattr(webbrowser, 'open', lambda x: x)
        writers.generator.generate(path=root, show=show)

    index = os.path.join(root, 'index.html')
    assert os.path.exists(index), str(index)
