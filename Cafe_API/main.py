from flask import Flask, jsonify, render_template,  request
from flask_sqlalchemy import SQLAlchemy

from random import choice
import pandas

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def serialize(self):
       """Return object data in easily serializable format"""

       return {'cafe':{
                    "can_take_calls":self.can_take_calls,
                        "coffee_price":self.coffee_price,
                        "has_scokets":self.has_sockets,
                        "has_toilet":self.has_toilet,
                        "has_wifi":self.has_wifi,
                        "id":self.id,
                        "img_url":self.img_url,
                        "location":self.location,
                        "map_url":self.map_url,
                        "name":self.name,
                        "seats":self.seats
                    }
                }

    def serialize_many(self,list:list):

        """Return list of object data in easily serializable format"""
        Dict = {'cafes':[]}

        for cafe in list:
            
            Dict['cafes'].append(cafe.serialize()['cafe'])

        return Dict

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Random Record
@app.route('/random',methods=['GET'])
def random():

    if request.method == "GET":

        #fetch random record from database 

        with app.app_context():

            #query random record 
            cafes = db.session.query(Cafe).all()
            random_record = choice(cafes)

            db.session.close()
        
            #serialize db object 

            return jsonify(random_record.serialize())


## HTTP GET - All Records
@app.route('/all',methods=['GET'])
def all():

    with app.app_context():

        #query all records
        all_cafes = db.session.query(Cafe).all()

        db.session.close()

        return jsonify(all_cafes[0].serialize_many(all_cafes))


## HTTP GET - Read Record
@app.route('/search',methods=['GET'])
def search():

    #get location parameter 
    loc_arg = request.args.get('loc',type=str)

    with app.app_context():

        query_response = db.session.query(Cafe).filter_by(location=loc_arg).first_or_404()

        db.session.close()

        return jsonify(query_response.serialize())

## HTTP POST - Create Record
@app.route('/add',methods=['GET','POST'])
def add():

    #get Cafe parameters
    
    name_arg = request.form.get('name')
    map_url_arg = request.form.get('map_url')
    img_url_arg = request.form.get('img_url')
    location_arg = request.form.get('location')
    seats_arg = request.form.get('seats')
    has_toilet_arg = bool(request.form.get('has_toilet'))
    has_wifi_arg = bool(request.form.get('has_wifi'))
    has_sockets_arg = bool(request.form.get('has_sockets'))
    can_take_calls_arg = bool(request.form.get('can_take_calls'))
    coffee_price_arg = request.form.get('coffee_price')

    with app.app_context():

        new_cafe = Cafe(
            name=name_arg,map_url=map_url_arg,img_url=img_url_arg,
            location=location_arg,seats=seats_arg,has_toilet=has_toilet_arg,
            has_wifi=has_wifi_arg,has_sockets=has_sockets_arg,can_take_calls=can_take_calls_arg,
            coffee_price=coffee_price_arg
        )

        try: 
            db.session.add(new_cafe)

            db.session.commit()

        except Exception as ex:

            db.session.close()

            return jsonify(response={'failed':"Cannot add your cafe, check input values again.",'error':str(ex)})
        
        return jsonify(response={'success':"Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
