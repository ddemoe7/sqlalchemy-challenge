# Weather Analysis
SQLAlchemy Assignment - Surfs Up!
<br>
<i>(sqlalchemy-challenge)</i>

## Background
Step 1 - Climate Analysis and Exploration
* Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration
* Use SQLAlchemy create_engine to connect to your sqlite database
* Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
* Link Python to the database by creating a SQLAlchemy session
* Don’t forget to close out your session at the end of your notebook

Precipitation Analysis
* Start by finding the most recent date in the data set
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data
* Select on the date and prcp values
* Load the query results into a Pandas DataFrame and set the index to the date column
* Sort the DataFrame values by date
* Plot the results using the DataFrame plot method

![precipitation](https://user-images.githubusercontent.com/22499952/119429386-baef3d00-bcdc-11eb-8d89-225bf16660b9.png)

Station Anaylsis
* Design a query to calculate the total number of stations in the datatset
* Design a query to find the most active stations

![temperature](https://user-images.githubusercontent.com/22499952/119429405-c04c8780-bcdc-11eb-8b46-4bc1b5349f20.png)

Step 2 - Climate App
* Now that you have completed your initial analysis, design a Flask API based on the queries you have developed
