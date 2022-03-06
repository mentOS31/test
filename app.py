from flask import Flask, jsonify, abort
from flask_restful import Api, Resource

app = Flask(__name__)

@app.route("/")
def abort_():
    return {}, 404

@app.route("/POST/")
    
if __name__ == '__main__':
    app.run()
