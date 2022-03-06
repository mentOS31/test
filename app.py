from flask import Flask, abort, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    making_time = db.Column(db.String(128), nullable=False)
    serves = db.Column(db.String(128), nullable=False)
    ingredients = db.Column(db.String(128), nullable=False)
    cost = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.String(128), nullable=False)
    updated_at = db.Column(db.String(128), nullable=False)
    

class User(Resource):
    def get(self):
        """
        ユーザを１件取得する
        """
        id = request.args.get('id')
        result = [n for n in users if n["id"] == id]

        if len(result) >= 1: 
            return result[0]
        else:
            abort(404)

    def post(self):
        """
        ユーザを登録する
        """
        #ユーザを追加
        db.session.add = (request.json)

        #正常に登録できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204


api.add_resource(User, '/user')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
