# Capstone project

## Purpose and Overview:

The purpose of this analysis is to explore whether there is a connection between country demographics, economic status, and military expenditures with terrorism in the last century. The completed analysis will be located on GitHub Pages and will contain interactive visualizations of the data including a map and web-scraped articles.

The reason this topic was selected was because it would enable us to work with large datasets full of information about many countries. Using these large datasets pertaining to country information and terrorism would allow us to use many techniques we learned throughout the course to transform the data as well as the flexibility to answer as many questions as possible. We thought that the topic itself was interesting to look into and we wanted to make sure that the datasets would not be too limiting in case there was unexpected technical difficulty in answering certain questions listed in the next section.

# Week 1

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

Due to the unstructured nature of our data, we determined that a non-relational database, such as Mongo DB, to house our data.  Mongo does not require a set schema which provides flexibility and its cloud based access is ideal for a distributed team.

Another benefit of Mongo is its ability to work with Jupyter Notebooks.  This allows for the data to be cleaned and transformed in a notebook and easily inserted into Mongo.

![upload to mongo](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/upload%20to%20mongo.png)

* Structure: Data Frames
Our primary data is drawn from 2 Kaggle datasets.  Each dataset has been uploaded into Mongo as a separate collection.  

![collection picture](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/raw%20data%20uploaded%20to%20mongo.png)

A document example from each collection is pictured below.  
![combined doc picture](https://github.com/namin1993/Capstone_Project/blob/lauren/lauren%20resources%20week%201/combined%20doc%20example.png)

The dataframes will be cleaned using Pandas.  Once cleaned, the data will be visually in a map using Mapbox and Leaflet.  Additional visualizations will be accomplished using Plotly.

* Structure: Web Scraping
During the next phase of this project we will scrape a news site containing recent articles regarding terrorism around the world.  Splinter and BeautifulSoup will be used to scrape the website and the results will be inserted into a dedicated Mongo collection for the scraped material.


## Week 1 Summary:
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






