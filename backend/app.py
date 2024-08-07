import os
from flask import Flask, render_template, send_from_directory, jsonify

from database_api.interfaces import select_all_users
from database_api.models import Users, Tasks, engine

from sqlalchemy.orm import sessionmaker

app = Flask("antikiller")
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/api', methods=['GET'])
def home():
    pass


@app.route('/tasks', methods=['GET'])
def get_tasks():
    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        all_tasks = session.query(Tasks).all()
        all_tasks_dict = [task.to_dict() for task in all_tasks]
    return jsonify(all_tasks_dict)


@app.route('/scoreboard', methods=['GET'])
def get_scoreboard():
    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        all_users = session.query(Users).all()
    all_users_dict = [user.to_dict() for user in all_users]

    return jsonify(all_users_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
