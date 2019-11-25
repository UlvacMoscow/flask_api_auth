from flask import Flask, jsonify
from config import Configuration
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)


users = []


class User(Resource):
    def get(self, name):
        for user in users:
            if user['name'] == name:
                return user
        return {'user': None}, 404

    def post(self, name):
        user = {'name': name, 'age': 18 }
        users.append(user)
        return user, 201

api.add_resource(User, '/user/<string:name>')



# users = [
#     {
#         'login' : 'Ben',
#         'active' : True,
#         'last coming': '20-11-2019',
#     }
# ]


#POST /auth data: {login , password}

# @app.route('/auth', methods=['POST'])
# def create_user():
#     pass

#GET /auth/<string:name>
# @app.route('/auth/<string:login>') #http://127.0.0.1:5000/auth/some_login
# def get_user():
#     pass

# GET /auth
# @app.route('/auth')
# def get_users():
#     return jsonify({'users' : users})
