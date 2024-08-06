import os
from flask import Flask, render_template, send_from_directory

app = Flask("quiz-tournament-registration")
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', message=f'ttt')
