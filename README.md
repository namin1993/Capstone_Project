# Segment 2


## Database Management

### [Cleaning Terror Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/cleaning_terror_df.ipynb): 

* First, I examined the CSV to ascertain the format of the data and formulate a gameplan for cleaning.  Next, I loaded the CSV into the notebook and continued examining the data.  Functions like ".head()"and ".dtypes" are useful to understand the structure.
![head and dyptes](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/head%20and%20dytpes.png)

* Using a loop to identify null values is also a helpful tactic to obtain information on the dataset.
![find nulls](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/find%20nulls.png)

* I conducted various transformations on the data set including:

      * dropping null values
			
      * changing columns like "INJURED" from float to integer since they present as integers in the original data
         
      * extracting the “year” from the DATE column by transforming it from an object to a date-time format 
        
      * transforming the "COORDINATES" column from an object to a string to use "str.split" to create a columns for latitude and longitude.   
                      
* An example of the "COORDINATES" transformation is pictured below.
![coordinates](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/coordinates.png)

* Once the cleaning process was complete, I upserted it as new collection in Mongo DB.
![upsert to mongo](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/upsert%20to%20mongo.png)


### [Cleaning CIA Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/cia_clean_v3.ipynb):

* Many of the examination steps noted above were repeated here. However, because this data set is considerably larger than the previous data set, I searched for columns likely to provide data to answer the questions posed in Segment 1.  This process reduced over 1100 columns to about 50 columns.

* Since I knew the pertinent columns,  I only loaded those columns into the notebook.
![column example]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/cia%20column%20names.png)

* As a strategy, I loaded the data as “string” data type because I anticipated using slicing as a method to retain necessary data and remove unwanted data.
![string]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/loaded%20as%20string.png)

* Next, I created an [exploartory notebook](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_df_explore.ipynb) to assist in determining how to slice the strings.

* In order to balance multiple priorities, I focused on creating a “[rough draft]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/intermed_clean_cia.csv)” data frame so my groupmates could access and begin to work with the data.

* The final data frame will be uploaded as collection to Mongo.  


### [New York Times (NYT) API](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_api/nyt_api_v_final.ipynb):

*  The purpose of this code is to provide interactivity to our final dashboard by allowing the user to view current NYT articles on terrorism.  We decided to use the API in lieu of other scrapping methods to avoid violating any site use terms that may exist. 

* The final code will return the article headline, date, lead paragraph, and a link to the NY Times article.

* An [exploratory notebook](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_api/nyt_api_explore_json.ipynb) was created to identify JSON targets for parsing.

* This process revealed that "abstract" and "snippet" returned the same information.
![abstract-snip](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/abstract%20and%20snippet.png)

* The [NY Times documentation](https://developer.nytimes.com/docs/articlesearch-product/1/overview) notes that searches are filtered using Lucene syntax. After a Google search, I installed [Luqum](https://luqum.readthedocs.io/en/latest/about.html) into my PythonData environment so I could narrow the search through filters.

* The completed code gathers the JSON targets and uploads them as a collection in Mongo.
