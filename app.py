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

    def post(self):
        """
        ユーザを登録する
        """
        if request.form.['id'] == 'None' :
            abort(404)
        if request.form.['title'] == 'None' :
            abort(404)
        if request.form.['making_time'] == 'None' :
            abort(404)
        if request.form.['serves'] == 'None' :
            abort(404)
        if request.form.['ingredients'] == 'None' :
            abort(404)
        if request.form.['cost'] == 'None' :
            abort(404)
        db.session.add = (request.json)

        return '', 200



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
