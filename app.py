from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

from models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app=app, db=db)

db.init_app(app=app)

api = Api(app=app)

jwt = JWTManager(app=app)

class SignUp(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        if username and password:
            new_user = User(username=username)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            return new_user.to_dict(), 201
        

class Login(Resource):
    def post(self):
        username = request.get_json()["username"]
        password = request.get_json()["password"]


        user = User.query.filter(User.username == username).first()

        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            
            return jsonify({"message": "Logged In Successfully", "access_token": access_token})
        
        else:
            return jsonify({"message": "Login Failed"}), 401

api.add_resource(SignUp, '/signup', endpoint="signup")
api.add_resource(Login, '/login', endpoint="login")

if __name__ == "__main__":
    app.run(port=5555, debug=True)