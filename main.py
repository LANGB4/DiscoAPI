from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class SightModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500))
    zip = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Sight(name = {self.name}, text = {self.text}, zip = {self.zip}'
        
'''
-- Initial setup of DB, only execute once! Overwrites entries...
with app.app_context():
    db.create_all()
'''

sight_put_args = reqparse.RequestParser()
sight_put_args.add_argument('name', type=str, help='name required..', location='form', required=True)
sight_put_args.add_argument('text', type=str, help='text required..', location='form', required=True)
sight_put_args.add_argument('zip', type=int, help='zip code required..', location='form', required=True)

sight_update_args = reqparse.RequestParser()
sight_update_args.add_argument('name', type=str, location='form')
sight_update_args.add_argument('text', type=str, location='form')
sight_update_args.add_argument('zip', type=int, location='form')


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'text': fields.String,
    'zip': fields.Integer
}


class Sights(Resource):

    @marshal_with(resource_fields)
    def get(self, sight_id):
        result = SightModel.query.filter_by(id=sight_id).first()
        if not result:
            abort(404, 'Sight id not found...')
        return result

    @marshal_with(resource_fields)
    def put(self, sight_id):
        args = sight_put_args.parse_args()
        result = SightModel.query.filter_by(id=sight_id).first()
        if result:
            abort(409, 'sigth id taken...')
        sight = SightModel(id=sight_id, name=args['name'], text=args['text'], zip=args['zip'])
        db.session.add(sight)
        db.session.commit()
        return sight, 201

    @marshal_with(resource_fields)
    def patch(self, sight_id):
        args = sight_update_args.parse_args()
        result = SightModel.query.filter_by(id=sight_id).first()
        if not result:
            abort(404, 'Sight id not found, cannot update...')
        if  args['name']:
            result.name = args['name']
        if args['text']:
            result.text = args['text']
        if args['zip']:
            result.zip = args['zip']
        db.session.commit()
        return result

    def delete(self, sight_id):
        print('------------delete called--------')   
        result = SightModel.query.filter_by(id=sight_id).first()
        if not result:
            abort(404, 'Sight id not found...')
        db.session.delete(result)
        db.session.commit()    
        return '', 204


api.add_resource(Sights, '/sight/<sight_id>')
if __name__ == '__main__':
    app.run(debug= True)
