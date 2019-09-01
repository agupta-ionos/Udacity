from flask import Flask, request, render_template, redirect, Response, jsonify
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine
from json import dumps
import os
#anubhav
db_connect = create_engine('sqlite:///tutorial.db')
app = Flask(__name__)
api = Api(app)

class Names(Resource):    
    def get(self):
        conn = db_connect.connect() # Connect to Database
        query = conn.execute("select * from RESTAURANT_DATA") # This line performs query and returns json result for all the Restaurants.
        return {'all': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} # Fetches all columns from the Table.
            
class PostNames(Resource):
    def get(self, DN):
        DM = DN
        conn = db_connect.connect() #Connect to Database
        query = conn.execute("select * from RESTAURANT_DATA where Dish_name like '%%%s%%' or Details like '%%%s%%'"%(DN,DM))  # This line performs query and returns json result for the particular Restaurant.
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    
# Actually setup the Api resource routing here
@app.route('/', methods=['GET'])
def worker():
    return render_template('Hotel.html')
    

api.add_resource(Names, '/all')
api.add_resource(PostNames, '/search/<DN>')


if __name__ == '__main__':
    app.run(debug='true')
