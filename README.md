# sqlalchemy-challenge

This assignment does basic exploration of climate anaylsis and data from a climate database provided by
several weather stations in Hawaii. We make use of SQLAlchemy in Jupyter notebook to explore and query the databse.
The use of auto_map base and the inspector are used to familiarize us with the data. After the anaysis is done, we make
use of Flask to design a Climate API based on the queries we have done.

###Precipitation Analysis:
A query was designed to retrieve the last twelve months of precipitation data. We first had to establish what the date ranges
of the database were, before selecting only the data and prcp values from the database.
The query results were sorted by date and loaded into a Pandas dataframe, with the index set to the date column.
A bar plot and the summary statistics for the precipitation data were done using Pandas.

###Station Analysis:
A query was designed to calculate the total number of stations in the database.



