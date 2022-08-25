# Capstone project

## Purpose and Overview:

The purpose of this analysis is to explore whether there is a connection between country demographics and terrorism.  The completed analysis will be located on GitHub Pages and will contain interactive visualizations of the data including a map and new articles obtained through either API or web-scraping.


# Segment 1

## Questions to Answer:

    1.) Which organizations are responsible for the most deaths and injuries from 1922-2022?
    2.) Which states/regions of a country had the most terrorist attacks from 1922-2022?
    3.) What is the demographic breakdown (gender percentage, percentage of each age range in a population, and percentage of urban people within a population) of each state where terrorism was committed?
    4.) What are the most common categories of terrorism within each region?
    5.) On what particular decade where the most terroist acts committed across the world?
    6.) What is the Economic Credit Rating for the regions where terrorism was inflicted?
    7.) What are the military expenditures where terrorism took place?
    8.) What are the specific Military organizations/treaties (check "Military and Security: Military - note" column) for each contry where terrorism took place?
    9.) What is the GDP breakdown for each country?
    
    
## Machine Learning:



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


## Segment 1 Summary:








