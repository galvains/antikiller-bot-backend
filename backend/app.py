import os
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask("antikiller")
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
def greeting():
    return render_template('index.html')
    # return jsonify({"message": "Hello from Flask!"})
