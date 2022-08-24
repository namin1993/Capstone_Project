# Capstone project

## Purpose and Overview:

The purpose of this analysis is to explore whether there is a connection between country demographics and terrorism.  The completed analysis will be located on GitHub Pages and will contain interactive visualizations of the data including a map and web-scraped articles.


# Week 1

## Questions to Answer:

*

*

*

## Machine Learning:



## Database Management & Visualizations:

Due to the unstructured nature of our data, we determined that a non-relational database, such as Mongo DB, to house our data.  Mongo does not require a set schema which provides flexibility and its cloud based access is ideal for a distributed team.

Another benefit of Mongo is its ability to work with Jupyter Notebooks.  This allows for the data to be cleaned and transformed in a notebook and easily inserted into Mongo.

![upload to mongo]

* Structure: Data Frames
Our primary data is drawn from 2 Kaggle datasets.  Each dataset has been uploaded into Mongo as a separate collection.  

![collection picture]

A document example from each collection is pictured below.  
![combined doc picture]

The dataframes will be cleaned using Pandas.  Once cleaned, the data will be visually in a map using Mapbox and Leaflet.  Additional visualizations will be accomplished using Plotly.

* Structure: Web Scraping
During the next phase of this project we will scrape a news site containing recent articles regarding terrorism around the world.  Splinter and BeautifulSoup will be used to scrape the website and the results will be inserted into a dedicated Mongo collection for the scraped material.


## Week 1 Summary:






