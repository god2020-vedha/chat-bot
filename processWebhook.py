import flask
import os
from flask import send_from_directory, request
from multiprocessing import Process
app = flask.Flask(__name__)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')

@app.route('/home')
def home():
    return "Hello World"



@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)

    return {
        'fulfillmentText': 'Yes dear .....tel me'
    }

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run(port=5002)
