from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='name required..', location='form')
parser.add_argument('text', type=str, help='text required..', location='form')
parser.add_argument('zip', type=int, help='zip code required..', location='form')

sights = {}

class Sights(Resource):

    def get(self, sight_id):
        return sights[sight_id]
    
    def put(self, sight_id):
        print('FORM---->',request.form)
        args = parser.parse_args()
        print('ARGS---->', args)
        return {sight_id: args}


api.add_resource(Sights, '/sight/<sight_id>')

if __name__ == '__main__':
    app.run(debug= True)
