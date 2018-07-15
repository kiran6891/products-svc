from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Products(Resource):

    def get(self):
        product = {
            "id": "MBP-1",
            "name": "MacBook Pro"
        }
        return product


api.add_resource(Products, "/products")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

