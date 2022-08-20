# Week 2


## Database Management

# [Terror Data Frame Cleaning](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/cleaning_terror_df.ipynb): 

* Prior to loading the CSV into Jupyter Notebook, I examined the CSV.  Once loaded into the notebook I used ".head()" to examine the structure and ".dtypes" to understand the type of data.
![head and dyptes](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/head%20and%20dytpes.png)

* Next, I looped through the data to find and print null values.
![find nulls](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/find%20nulls.png)

* I dropped the null values so that the errors would not occur with the visualizations.

* Next, I changed the "INJURED" and "DEAD" columns from float to integer since they present as integers in the original CSV format.

* I changed the "DATE" column from an object to a date-time format so that I could extract the year value and add it as a column to the finished data frame.

* I transformed the "COORDINATES" column from an object to a string so that I could use "str.split" to create a column for latitude and a column for longitude.
![coordinates](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/coordinates.png)

* Finally, I re-ordered the columns into a data frame and upserted it as new collection in Mongo DB.
![upsert to mongo](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/upsert%20to%20mongo.png)
