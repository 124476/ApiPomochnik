from datetime import datetime

import flask
from flask import jsonify

from data import db_session
from data.meropriation import Meropriation

blueprint = flask.Blueprint(
    'meropriations_api',
    __name__,
    template_folder='templates'
)

db_session.global_init('db/Dbase.db')


@blueprint.route('/api/meropriations/<int:meropriation_id>')
def get_meropriation(meropriation_id):
    db_sess = db_session.create_session()

    meropriation = db_sess.query(Meropriation).filter(Meropriation.id == meropriation_id).first()
    a = {
        "id": meropriation.id,
        "name": meropriation.name,
        "date": meropriation.date,
    }
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/meropriations')
def get_meropriations():
    db_sess = db_session.create_session()
    a = []
    for i in db_sess.query(Meropriation):
        a.append({
            "id": i.id,
            "name": i.name,
            "date": i.date,
        })
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/meropriations/add/<string:name>/<string:date>')
def add_meropriation(name, date):
    db_sess = db_session.create_session()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    merop = Meropriation(name=name,
                         date=date)
    db_sess.add(merop)
    db_sess.commit()
    db_sess.close()
    return jsonify({
        "status": "ok"
    })


@blueprint.route('/api/meropriations/set/<int:merop_id>/<string:name>/<string:date>')
def set_meropriation(merop_id, name, date):
    db_sess = db_session.create_session()
    merop = db_sess.query(Meropriation).filter(Meropriation.id == merop_id).first()
    if merop:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        merop.name = name
        merop.date = date
        db_sess.commit()
    db_sess.close()
    return jsonify({
        "status": "ok"
    })


@blueprint.route('/api/meropriations/del/<int:merop_id>')
def del_meropriation(merop_id):
    db_sess = db_session.create_session()
    merop = db_sess.query(Meropriation).filter(Meropriation.id == merop_id).first()
    if merop:
        db_sess.delete(merop)
        db_sess.commit()
    db_sess.close()
    return jsonify({
        "status": "ok"
    })
