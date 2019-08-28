# SQL-Alchemy
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


Using the hawaii.sqlite files to complete my climate analysis and data exploration.
Choose a start date and end date for my trip. Make sure that my vacation range is approximately 3-15 days total.
Use SQLAlchemy create_engine to connect to my sqlite database.
Use SQLAlchemy automap_base() to reflect my tables into classes and save a reference to those classes called Station and Measurement.



Precipitation Analysis


Design a query to retrieve the last 12 months of precipitation data.
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.
Use Pandas to print the summary statistics for the precipitation data.



Station Analysis


Design a query to calculate the total number of stations.

Design a query to find the most active stations.


List the stations and observation counts in descending order.
Which station has the highest number of observations?
Hint: You may need to use functions such as func.min, func.max, func.avg, and func.count in your queries.



Design a query to retrieve the last 12 months of temperature observation data (tobs).


Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12.


Temperature Analysis (Optional)


Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

Plot the min, avg, and max temperature from your previous query as a bar chart.


Use the average temperature as the bar height.
Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).






