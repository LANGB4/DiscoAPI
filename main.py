from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

sight_put_args = reqparse.RequestParser()
sight_put_args.add_argument('name', type=str, help='name required..', location='args')
sight_put_args.add_argument('text', type=str, help='text required..', location='args')
sight_put_args.add_argument('zip', type=int, help='zip code required..', location='args')

sights = {}

class Sights(Resource):
    def get(self, sight_id):
        return sights[sight_id]
    
    def put(self, sight_id):
        print('FORM---->',request.form)
        args = sight_put_args.parse_args()
        print('ARGS---->', args)
        return {sight_id: args}


api.add_resource(Sights, '/sight/<int:sight_id>')

if __name__ == '__main__':
    app.run(debug= True)
