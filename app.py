from flask import Flask

app = Flask(__name__)

@app.route("/")
abort(404)    

if __name__ == '__main__':
    app.run()
