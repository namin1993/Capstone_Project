# Segment 2


## Database Management

### [Cleaning Terror Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/cleaning_terror_df.ipynb): 

* First, I examined the CSV to ascertain the format of the data and formulate a gameplan for cleaning.  Next, I loaded the CSV into the notebook and continued examining the data.  I used functions like ".head()"and ".dtypes" to understand the structure.

	![head and dyptes](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/head%20and%20dytpes.png)

* Here, I used a loop to identify null values in the dataset.
![find nulls](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/find%20nulls.png)

* Various transformations were conducted including:

      * dropping null values
			
      * changing columns like "INJURED" from float to integer since they present as integers in the original data
         
      * extracting the “year” from the DATE column by transforming it from an object to a date-time format 
        
      * transforming the "COORDINATES" column from an object to a string to use "str.split" to create a columns for latitude and longitude.   
                      
* An example of the "COORDINATES" transformation is pictured below.
![coordinates](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/coordinates.png)

* Once the cleaning process was complete, I upserted it as new collection in Mongo DB.
![upsert to mongo](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/upsert%20to%20mongo.png)


### [Cleaning CIA Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia.ipynb):

* Many of the examination steps noted above were repeated [here](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_df_explore.ipynb). 

* Since this data set is considerably larger than the previous data set, I began by searching the original data for columns likely the answers the questions posed in Segment 1.  

* Once I ascertained the pertinent columns, I only loaded those columns into an [exploratory notebook](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_df_explore.ipynb).
![column example]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/cia%20column%20names.png)

* Many columns contained multiple data points that needed to be moved into separate columns in order to work with that data.

	![orig pic]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/example%20of%20data%20gdp.png)

* My initial strategy was to use slicing in Python to slice the data and move into separate columns.  However, this cause an issue with leading and trailing characters, similar to the trailing periods shown below.
![lead and trail]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/example%20of%20trailing.png)

* This caused a change in strategies.  I exported the data as a CSV and used Excel’s “text to columns” feature to make slices in the data where needed.  Additionally, there were some non-conforming number formats, which I edited directly in Excel rather than using Python.  

* Since the original data was not presented in a format where I could use a loop or function to repeat the same process and because there were only a handful of non-conforming formats,  working in Excel was more efficient than working in Python.

* Once this process was complete, I loaded the final data into a notebook and uploaded it as a collection to Mongo.  

### [Join Data Frames](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_join_lang_relig.ipynb)

* The final data frame is comprised of 3 data frames.

* First, the [Languages data frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_language.ipynb) and the [Religions data frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_religion.ipynb) were cut from the CIA data frame.  

* Both data frames show country information in conjunction with demographic information and   were uploaded Mongo in their separate forms.
![Mongo join](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/mongo_join.png)

* The Religion and Languages data frames were downloaded from Mongo and incorporated into a new notebook and were joined.  Next, the clean_terror_df was loaded into the notebook and manipulated to show the terror acts on a per country basis.   

* The final data frame shows the demographic information alongside the terrorist acts per country.
![final df](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/join%20df%20example.png)



### [New York Times (NYT) API](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_api/nyt_api_v_final.ipynb):

*  The purpose of this code is to provide interactivity to our final dashboard by allowing the user to view current NYT articles on terrorism.  We decided to use the API in lieu of other scrapping methods to avoid violating any site use terms that may exist. 

* The final code will return the article headline, date, lead paragraph, and a link to the NY Times article.

* An [exploratory notebook](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_api/nyt_api_explore_json.ipynb) was created to identify JSON targets for parsing.

* This process revealed that "abstract" and "snippet" returned the same information.
![abstract-snip](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/abstract%20and%20snippet.png)

* The [NY Times documentation](https://developer.nytimes.com/docs/articlesearch-product/1/overview) notes that searches are filtered using Lucene syntax. After a Google search, I installed [Luqum](https://luqum.readthedocs.io/en/latest/about.html) into my PythonData environment so I could narrow the search through filters.

* The completed code gathers the JSON targets and uploads them as a collection in Mongo.
