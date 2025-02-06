import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return {
        'msg': 'Hello World! This is a simple Python app using Flask! But wait there is more!',
        'endpoints': ['/', '/ping', '/debug', '/debug/ui']
    }


@app.route('/ping')
def ping():
    return {'msg': 'pong!'}
    

if __name__ == '__main__':
    port = os.environ.get('PORT', 5001)
    app.run(debug=True, host='0.0.0.0', port=port)
