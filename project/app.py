from flask import Flask, jsonify
from config import Configuration



app = Flask(__name__)

users = [
    {
        'login' : 'Ben',
        'active' : True,
        'last coming': '20-11-2019',
    }
]


#POST /auth data: {login , password}

@app.route('/auth', methods=['POST'])
def create_user():
    pass

#GET /auth/<string:name>
@app.route('/auth/<string:login>') #http://127.0.0.1:5000/auth/some_login
def get_user():
    pass

# GET /auth
@app.route('/auth')
def get_users():
    return jsonify({'users' : users})
