import flask
from flask import jsonify

from data import db_session
from data.git import Git
from data.version import Version

blueprint = flask.Blueprint(
    'git_api',
    __name__,
    template_folder='templates'
)

db_session.global_init('db/Dbase.db')


@blueprint.route('/api/gites/<int:gitId>')
def get_git(gitId):
    db_sess = db_session.create_session()

    a = []
    for i in db_sess.query(Version).filter(Version.git_id == gitId):
        a.append({
            "id": i.id,
            "text": i.text,
            "number": i.number,
        })

    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/gites')
def get_gites():
    db_sess = db_session.create_session()
    a = []
    for i in db_sess.query(Git):
        a.append({"id": i.id,
                  "name": i.name
                  })
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/gites/<int:gitId>/<int:number>')
def get_version(gitId, number):
    db_sess = db_session.create_session()
    version = db_sess.query(Version).filter(Version.git_id == gitId).filter(Version.number == number).first()
    a = {
        "id": version.id,
        "git_id": version.git_id,
        "number": version.number,
        "text": version.text,
    }
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/gites/add/<string:nameGit>')
def add_git(nameGit):
    db_sess = db_session.create_session()
    git = db_sess.query(Git).filter(Git.name == nameGit).first()
    if not git:
        git = Git(name=nameGit)
        db_sess.add(git)
        db_sess.commit()
    db_sess.close()
    return jsonify({
        "status": "ok"
    })


@blueprint.route('/api/gites/<int:idGit>/add/<string:text>')
def add_version(idGit, text):
    db_sess = db_session.create_session()
    git = db_sess.query(Git).filter(Git.id == idGit).first()
    if not git:
        return
    versionLast = db_sess.query(Version).filter(Version.git_id == idGit)
    number = 1
    if versionLast:
        ln = 0
        for _ in versionLast:
            ln += 1
        number = ln + 1

    ver = Version(
        git_id=idGit,
        number=number,
        text=text,
    )

    db_sess.add(ver)
    db_sess.commit()
    db_sess.close()
    return jsonify({
        "status": "ok"
    })
