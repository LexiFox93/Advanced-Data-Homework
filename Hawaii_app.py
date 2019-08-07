from flask import flask, json, jsonify
from db_prepare import engine, func, session, Measurement, Station
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

#db setup
engine = create_engine("sqlite:///hawaii.sqlite")
print("You are now connected to the Hawaii Weather database")

 # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

 # Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a Flask app
app=Flask(__name__)

##########################################
#Flask Routes
##########################################

#define what to do when user hits index route
@app.route("/")
def welcome():
    """List all available API routes"""
    return (
        f"Precipition Information:<br/>"
        f"Stations Information:<br/>"
        f"Temperature Data:<br/>"
        f"More Temperature data:<br/>"
        f"Some other Temperature data that I have no idea how to get:<br/>"
    )

#define what to do when user selects /api/v1.0/precipitation
@app.route('/api/v1.0/precipitation/')
def precipitation():
    session = Session(engine)
    prcp_info = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= '2017-08-23').all()
    prcp_dict=dict(prcp_info)
    print()
    print("Precipitation results")
    return jsonify(prcp_dict)

#define what to do when user selects /api/v1.0/stations
@app.route('/api/v1.0/station/')
def station():
    session = Session(engine)
    station_info = session.query(Station.station).\
    order_by(Station.station).all()
    print()
    print("Station results")
    for row in station_list:
        print (row[0])
    return jsonify(station_list)

#define what to do when user selects /api/v1.0/tobs
@app.route('/api/v1.0/tobs/')
def tobs():
    session = Session(engine)
    tobs_info = session.query(Measurement.tobs).\
    order_by(Measurement.tobs).all()
    print()
    print("Temperature Results")
    return jsonify(tobs_info)

#define what to do when user selects /api/v1.0/<start>
@app.route('/api/v1.0/<start>/')
def start():
    session = Session(engine)
    start_info = session.query(station.id,
                        station.station,
                        func.min(Measurement.tobs),
                        func.max(Measurement.tobs),
                        func.avg(Measurement.tobs),
                        filter(Measurement.station) == Station.station).\
                        filer(Measurement.date>=start).all()
        )
    #seriously...i have no idea at all what to do now...


#define what to do when user selects /api/v1.0/<start>/<end>
@app.route('/api/v1.0/<start>/<end>/')
def start_end():
    #no idea what to do now and guess what...don't care either...this just sucks!!!


    
if__name__=="__main__":
    app.run(debug=True)