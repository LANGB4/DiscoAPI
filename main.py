from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

sights = {}

class Sights(Resource):
    def get(self, sight_id):
        return sights[sight_id]

api.add_resource(Sights, '/sight/<int:sight_id>')

if __name__ == '__main__':
    app.run(debug= True)
