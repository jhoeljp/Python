from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

from random import randint

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


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/random',methods=['GET'])
def random():

    if request.method == "GET":

        #fetch random record from database 

        with app.app_context():

            #get id range available
            max_id = db.session.query(Cafe).order_by(Cafe.id.desc()).first()
            min_id = db.session.query(Cafe).order_by(Cafe.id.asc()).first()
            
            random_id = randint(min_id.id,max_id.id)

            #query random record 
            random_record = db.session.query(Cafe).filter_by(id=random_id).one()

            db.session.close()
        
            #serialize db object 
            return jsonify(
                {'cafe':{
                    "can_take_calls":random_record.can_take_calls,
                    "coffee_price":random_record.coffee_price,
                    "has_scokets":random_record.has_sockets,
                    "has_toilet":random_record.has_toilet,
                    "has_wifi":random_record.has_wifi,
                    "id":random_record.id,
                    "img_url":random_record.img_url,
                    "location":random_record.location,
                    "map_url":random_record.map_url,
                    "name":random_record.name,
                    "seats":random_record.seats
                    }
                }
            )


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
