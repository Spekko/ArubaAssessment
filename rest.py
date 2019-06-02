from flask import Flask, request
from flask_restful import Resource, Api
from helperFunctions import Functions
import requests_cache
from waitress import serve

app = Flask(__name__)
api = Api(app)


class scanRest(Resource):
    def post(self):
        args = request.get_json()

        parser = Functions()
        try:
            dataExtract = parser.parse(args)
        except:
            return("invalid apscan")


        location = parser.getLocation(dataExtract)

        return location


api.add_resource(scanRest, '/scan')

if __name__ == '__main__':
    #app.run(port='8080')
    try:
        serve(app, port=8080)
    except:
        print("server failed")
