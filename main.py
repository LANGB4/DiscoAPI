from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

sight_parser = reqparse.RequestParser()
sight_parser.add_argument('name', type=str, help='name required..', location='form', required=True)
sight_parser.add_argument('text', type=str, help='text required..', location='form', required=True)
sight_parser.add_argument('zip', type=int, help='zip code required..', location='form', required=True)

sights = {}

def abort_if_not_exists(sight_id):
    if sight_id not in sights:
        abort(404, 'sight_id not valid...')

def abort_if_exists(sight_id):
    if sight_id in sights:
        abort(409, 'sight_id already exists...')

class Sights(Resource):

    def get(self, sight_id):
        abort_if_not_exists(sight_id)
        return sights[sight_id]

    
    def put(self, sight_id):
        abort_if_exists(sight_id)
        print('FORM---->',request.form)
        args = sight_parser.parse_args()
        print('ARGS---->', args)
        sights[sight_id] = args
        return sights[sight_id], 201

    def delete(self, sight_id):
        abort_if_not_exists(sight_id)
        del sights[sight_id]
        return sight_id + 'deleted', 204



api.add_resource(Sights, '/sight/<sight_id>')

if __name__ == '__main__':
    app.run(debug= True)
