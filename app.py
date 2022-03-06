from flask import Flask, abort, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe.db'
db = SQLAlchemy(app)
api = Api(app)

class recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    making_time = db.Column(db.String(50), nullable=False)
    serves = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    updated_at  = db.Column(db.String(50), nullable=False)


class User(Resource):
    def post(self):
        
        users.append(request.json)

        #正常に登録できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204
    
    def get(self):
        """
        ユーザを１件取得する
        """
        id = request.args.get('id')
        result = [n for n in users if n["id"] == id]

        if len(result) >= 1: 
            # ユーザ情報を返却
            return result[0]
        else:
            # 存在しないユーザIDが指定された
            abort(404)
    

    def put(self):
        """
        ユーザを更新する
        """
        user = request.json
        lst = [val for val in users if val["id"] == user["id"]]
        
        if len(lst) >= 1: 
            lst[0]["name"] = user["name"]
            lst[0]["age"] = user["age"]
        else:
            #存在しないユーザIDが指定された場合
            abort(404)

        #正常に更新できたので、HTTP status=204(NO CONTENT)を返す
        return '', 204

    def delete(self):
        """
        ユーザを削除する
        """
        id = request.args.get('id')
        lst = [i for i, val in enumerate(users) if val["id"] == id]
        for index in lst:
            del users[index]

        if len(lst) >= 1: 
            #ユーザの削除を行った場合、HTTP status=204(NO CONTENT)を返す
            return '', 204
        else:
            #存在しないユーザIDが指定された場合
            abort(404)

api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(debug=True)
