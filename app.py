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
    

@app.route('/', methods=['POST'])
def post():
    if request.form.get('id') == 'None'
        abort(404)
    if request.form.get('title') == 'None'
        abort(404)
    if request.form.get('making_time') == 'None'
        abort(404)
    if request.form.get('serves') == 'None'
        abort(404)
    if request.form.get('ingredients') == 'None'
        abort(404)
    if request.form.get('cost') == 'None'
        abort(404)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
