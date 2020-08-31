# import Flask and other dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
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
        f"Welcome to my Hawaii Weather Station API! Available Routes :<br/>"
        f"<a href='/api/v1.0/precipitation'>precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>station</a><br/>"
        f"<a href='/api/v1.0/tobs'>tobs</a><br/>"
        f"<a href='/api/v1.0/start'>start</a><br/>"
        f"<a href='/api/v1.0/start/end'>start/end</a><br/>"
        
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the precipitation data of the last twelve months including date and prcp values """
    # Query all precipitation data for last twelve months
    date = dt.datetime(2016, 8, 22)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > date).order_by(Measurement.date).all()
                                                                     
    session.close()

    # Create a dictionary from the row data and append to a list of year_precipitation
    year_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        year_precipitation.append(precipitation_dict)

    return jsonify(year_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list(good practice to close session/housekeeping) 
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all tobs from the most active station for the previous year"""
    # Query all stations
    date = dt.datetime(2016, 8, 17)

    results = session.query(Measurement.tobs).filter(Measurement.date > date).\
    filter(Measurement.station == 'USC00519281').all()

    session.close()
   
     # Convert list of tuples into normal list(good practice to close session/housekeeping) 
    tobs = list(np.ravel(results))
  
    return jsonify(tobs)    

#@app.route("/api/v1.0/<start>")
#def start(start):

# Create our session (link) from Python to the DB
    #session = Session(engine)

"""TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    #return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        #filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()







#@app.route("/api/v1.0/<start>/<end>")



if __name__ == '__main__':
    app.run(debug=True)

                                                  