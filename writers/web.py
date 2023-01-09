# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask
import jinja2
import utila

import writers

welcome = flask.Blueprint('welcome', __name__)  # pylint:disable=invalid-name


@welcome.route('/', defaults={'page': 'index.html'})
@welcome.route('/<path:page>')
def show_welcome(page):
    """Route public pages which are visible without any permissions."""
    try:
        return flask.render_template(f'{page}')
    except jinja2.TemplateNotFound:
        return flask.render_template('index.html', errorpage=page)


def create(path: str = None) -> flask.Flask:
    # Flask determines template- and static-folder automatically.
    templates = writers.build() if path is None else path
    static = os.path.join(templates, '_static')
    utila.log(f'template folder: {writers.build()}')
    result = flask.Flask(
        __name__,
        template_folder=templates,
        static_folder=static,
    )

    result.register_blueprint(welcome)

    return result


def run():
    utila.log('run webserver')
    app = create()
    app.run(port=writers.PORT)
    return utila.SUCCESS
