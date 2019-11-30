from flask import Flask, jsonify, request
from config import Configuration
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity



app = Flask(__name__)
app.secret_key = 'sen'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

users = []


class User(Resource):
    @jwt_required()
    def get(self, name):
        user = next(filter(lambda x: x['name'] == name, users), None)
        return {'user': user}, 200 if user else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, users), None): # is not None
            return {'message' : 'user with so name {} already registred'.format(name)}, 400
        data = request.get_json()
        user = {'name': name, 'age': data['age']}
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = list(filter(lambda x: x['name'] != name, users))
        return {'message' : 'item deleted'}

    def put(self, name):
        # global users
        data = request.get_json()
        user = next(filter(lambda x: x['name'] != name, users), None)
        if user is None:
            user = {'name': name, 'price': data['price']}
            users.append(user)
        else:
            user.update(data)
        return user



class UserList(Resource):
    def get(self):
        return {'users': users}

api.add_resource(User, '/user/<string:name>')
api.add_resource(UserList, '/users')


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
