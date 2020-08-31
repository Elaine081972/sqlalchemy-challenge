# sqlalchemy-challenge

This assignment does basic exploration of climate anaylsis and data from a climate database provided by
several weather stations in Hawaii. We make use of SQLAlchemy in Jupyter notebook to explore and query the sqlite databse.
The use of auto_map base and the inspector are used to familiarize us with the data. After the anaysis is done, we make
use of Flask to design a Climate API based on the queries we have done. The code is in an app.py file that allows a path to the database for queries that are static and dynamic.

###Precipitation Analysis:
A query was designed to retrieve the last twelve months of precipitation data. We first had to establish what the date ranges
of the database were, before selecting only the data and prcp values from the database.
The query results were sorted by date and loaded into a Pandas dataframe, with the index set to the date column.
A bar plot and the summary statistics for the precipitation data were done using Pandas.

###Station Analysis:
A query was designed to calculate the total number of stations in the database. Further queries were designed around the temperature
observation data(TOBS). A list of the stations with their total observation counts in descending order were found. This then allowed us to further explore the most "active" station (USC00519281). The last twelve months of TOBS data for this particular station was retrieved and then plotted as a histogram.

###Climate App:

Flask was used to create our routes for our Hawaii weather API. A home page was created with five different routes:
1. precipatation query that returns date and prcp in JSON format of the dictionary
2. station query that returns list of stations in JSON
3. tobs - JSON list of the temperature observations for the last year of the most active station
4. start TOBS - dynamic query that when a start date is entered in the URL - TMIN, TAVG, TMAX are returned in JSON for start date through all dates greater
5. start/end TOBS - dynamic query that builds on the one above. Provides the same TMIN, TAVG, TMAX in JSON, but for a range of dates that are entered in the URL









