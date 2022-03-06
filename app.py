from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route("/")
def abort_():
    abort(404)

if __name__ == '__main__':
    app.run()
