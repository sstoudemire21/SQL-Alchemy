import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
print(Base.classes.keys())
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/api/v1.0/")
@app.route("/")

def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation"
        "<br/>"
        "/api/v1.0/stations"
        "<br/>"
        "/api/v1.0/tobs"
        "<br/>"
        "/api/v1.0/<start>"
        "<br/>"
        "/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def data():
    # Query all date & prcp
    prior_yr = dt.date(2017, 8, 22)-dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(func.strftime(Measurement.date >= prior_yr)).all()

    data_info = {date: prcp for date, prcp in results}
    
    return jsonify(data_info)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    sta_name = list(np.ravel(results))


    return jsonify(sta_name)

@app.route("/api/v1.0/tobs")
def temperature():
    results = session.query(Measurement.tobs).all()

    temp = list(np.ravel(results))

    return jsonify(temp)

@app.route("/api/v1.0/<start>")
def start_date(start=None):

   
   results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
   filter(Measurement.date >= start).all()
    
    
   start_dt = list(np.ravel(results))
   return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start=None, end=None):
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).group_by(Measurement.date).all()

    end_date = list(np.ravel(results))

    return jsonify(end_date)

 

if __name__ == "__main__":
    app.run(debug=True)




