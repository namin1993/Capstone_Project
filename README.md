# Capstone project

## Purpose and Overview:

The purpose of this analysis is to explore whether there is a connection between country demographics, economic status, and military expenditures with terrorism in the last century. The completed analysis will be located on GitHub Pages and will contain interactive visualizations of the data including a map and web-scraped articles.

The reason this topic was selected was because it would enable us to work with large datasets full of information about many countries. Using these large datasets pertaining to country information and terrorism would allow us to use many techniques we learned throughout the course to transform the data as well as the flexibility to answer as many questions as possible. We thought that the topic itself was interesting to look into and we wanted to make sure that the datasets would not be too limiting in case there was unexpected technical difficulty in answering certain questions listed in the next section.

# Segment 1:

## Questions to Answer:

    1.) Which organizations are responsible for the most deaths and injuries from 1922-2022?
    2.) Which regions/subregions of a country had the most terrorist attacks from 1922-2022?
    3.) What is the demographic breakdown (gender percentage, percentage of each age range in a population, and percentage of urban people within a population) of each state where terrorism was committed?
    4.) What are the most common categories of terrorism within each region?
    5.) On what particular decade where the most terroist acts committed across the world?
    6.) What is the Economic Credit Rating for the regions where terrorism was inflicted?
    7.) What are the military expenditures where terrorism took place?
    8.) What are the specific Military organizations/treaties (check "Military and Security: Military - note" column) for each contry where terrorism took place?
    9.) What is the GDP breakdown for each country?
    
## Machine Learning:

The "db_connections.py" file was created solely for connecting to the database and its collections. By creating a python file specifically for database connections, we would have the flexibility to import the db_connections module into other python files for different parts of our code. If there were any new MongoDB collections to add to our code, we would only need to alter the db_connections.py file instead of tracking down database connection code used throughout any of our files.

The ml_modeling_rough_draft.ipynb visually shows the success in connecting to the Cloud Mongo DB collection called "cleaned_terror_df". The rough draft machine learning code contains all of the required imports as well as a general transformation-action outline for agglomerative hierarchical clustering of terrorist attacks. We chose this machine-learning model in order to identify which attacks appeared to be similar to one another in outcome.


## Database Management & Visualizations:

We determined that a non-relational database, such as Mongo DB, is the best solution to house our data due to its unstructured nature.  Mongo does not require a set schema which provides flexibility and its cloud based access is ideal for a distributed team.  Mongo works well with Jupyter Notebooks, allowing for easy upload, cleaning, and transformation of the data.

An example of the upload code is pictured below.
![upload to mongo](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/upload%20to%20mongo.png)

Our primary data is drawn from 2 Kaggle datasets.  The CIA dataset contains around 1100 columns and 250 rows.  By contrast, the Terror dataset comprises 12 columns and over 27000 rows. Each dataset has been uploaded into Mongo as a separate collection.  

![collection picture](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/raw%20data%20uploaded%20to%20mongo.png)

A document example from each collection is pictured below.  
![combined doc picture](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/combined%20doc%20example.png)

Each collection holds a range of datatypes, including objects, strings, integrers, and floats.  The dataframes will be cleaned using Pandas.  Once cleaned, the data will be visualized in a map using Mapbox and Leaflet.  Additional visualizations will be accomplished using Plotly.

## Web Scraping:
During the next phase of this project we will scrape a news site containing articles regarding terrorism around the world.  The results will be inserted into a dedicated Mongo collection for the scraped material and our final dashboard will pull the articles from Mongo.


## Segment 1 Summary:
Our team regularly updated each other on Slack and outlined talking points prior to our Zoom meeting. Any questions would be addressed on our Zoom meeting.

8/16 - 8/21
    * Assigning roles that we would keep for the duration of the project
    * Clarifying what the capstone project would require from the 1st week submission and the final submission
    * Establishing proper protocol for GitHub Repository Management
    * Deciding on the topic and datasets
    * Deciding on the database structure
    * Creating a proper directory setup and code templates for the project

8/23 - 8/28
The 2nd group meeting on 8/23 were as outlined:
    Gameplan for 8/23:
    * Review data upload and connection to database
    * Review code template mock-up
    * Review questions
    
    Objectives from 8/23 - 8/28
    * Finish objectives for First Submission 8/28
    * Upload more data onto database
    * Work on scraping articles and images from a good website
    * Work on coding for machine learning and answering questions
    * Find a good bootstrap4/html/css webpage template

# Segment 2


## Database Management

### [Cleaning Terror Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/cleaning_terror_df.ipynb): 

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
