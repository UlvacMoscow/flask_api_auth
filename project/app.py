from flask import Flask
from config import Configuration


app = Flask(__name__)


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
    pass
