# Import Flask
from flask import Flask, jsonify

# Dependencies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"Precipitation Analysis:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"Station Analysis:<br/>"
        f"/api/v1.0/stations<br/>"
        f"Temperature Analysis:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Start Day Analysis:<br/>"
        f"/api/v1.0/start<br/>"
        f"Start and End Day Analysis:<br/>"
        f"/api/v1.0/start/end"

    )

# Precipitation Route
@app.route("/api/v1.0/precipitation") #Convert query results to a dictionary using `date` as the key and `tobs` as the value
def precipitation():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query Measurement
    results = (session.query(Measurement.date, Measurement.tobs)
                      .order_by(Measurement.date))
    
    # Create a dictionary
    precipitationDateTobs = []
    for each_row in results:
        DateTobs_dict = {}
        DateTobs_dict["date"] = each_row.date
        DateTobs_dict["tobs"] = each_row.tobs
        precipitationDateTobs.append(DateTobs_dict)

    return jsonify(precipitationDateTobs)

# Station Route
@app.route("/api/v1.0/stations") #Return a JSON list of stations from the dataset
def stations():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query Stations
    results = session.query(Station.name).all()

    # Convert list of tuples into normal list
    stationDetails = list(np.ravel(results))

    return jsonify(stationDetails)

# TOBs Route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperatures for prior year"""
#    * Query for the dates and temperature observations from the last year.
#           * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
#           * Return the json representation of your dictionary.
    lastDate = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    lastYear = DateTobs.date(2017, 8, 23) - DateTobs.timedelta(days=365)
    temperature = session.query(Measurements.date, Measurements.tobs).\
        filter(Measurements.date > lastYear).\
        order_by(Measurements.date).all()

# Create a list of dicts with `date` and `tobs` as the keys and values
    temperatureTotals = []
    for result in temperature:
        row = {}
        row["date"] = temperature[0]
        row["tobs"] = temperature[1]
        temperatureTotals.append(row)

    return jsonify(temperatureTotals)

# Start Day Route
@app.route("/api/v1.0/<start>")
def trip1(start):

 # go back one year from start date and go to end of data for Min/Avg/Max temp   
    startDate= dt.datetime.strptime(start, '%Y-%m-%d')
    lastYear = dt.timedelta(days=365)
    start = startDate-lastYear
    end =  DateTobs.date(2017, 8, 23)
    tripData = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    trip = list(np.ravel(tripData))
    return jsonify(trip)

# Start-End Day Route
@app.route("/api/v1.0/<start>/<end>")
def trip2(start,end):

  # go back one year from start/end date and get Min/Avg/Max temp     
    startDate= DateTobs.datetime.strptime(start, '%Y-%m-%d')
    endDate= DateTobs.datetime.strptime(end,'%Y-%m-%d')
    lastYear = DateTobs.timedelta(days=365)
    start = startDate-lastYear
    end = endDate-lastYear
    tripData = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    trip = list(np.ravel(tripData))
    return jsonify(trip)

# Define Main Behavior
if __name__ == '__main__':
    app.run(debug=True)