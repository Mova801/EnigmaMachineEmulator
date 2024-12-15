from flask import render_template, flash

from app.main import bp


@bp.get('/index/')
@bp.get('/')
def index() -> str:
    flash('Enigma Machine Simulator')
    return render_template('index.html', method='GET')


def index_post() -> str:
    flash('<MSG_ID>', category='success')
    return render_template('index.html', method='POST')
