# Webscraping
# Import Dependencies
import requests
from config import api_key
import time
import json
import pandas as pd
from luqum.parser import parser 

# Initiate scrape_all() to receive data
def scrape_all():
    try:
        # Set variables for query
        #replace the query variable with the parser ('(title:"foo bar" AND body:"quick fox") OR title:fox')
        desk = parser.parse('(news_desk:"Foreign" "World" "Business" "Financial" "Politics" "Travel" "U.S." AND source: "The New York Times")')
        query = "terror* OR bomb"

        #save url
        url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

        #set search dates
        begin_date = "20170101"
        # make end_date a parameter
        end_date = "20221231"

        # Build query URL & sorted query to newest
        query_url = f"{url}api-key={api_key}&q={query}&fq={desk}&sort=newest&begin_date={begin_date}&end_date={end_date}"

        # Empty list for articles
        articles_list = []

        # loop through pages, 10 results per page
        for page in range(0, 2):
            # create query with page number
            query_url = f"{query_url}&page={str(page)}"
            articles = requests.get(query_url).json()
            
            # Add a one second interval between queries to stay within API query limits
            time.sleep(1)
            # loop through the response and append each article to the list
            for article in articles["response"]["docs"]:
                articles_list.append(article)

        # Create loop to collect dictionary objects with certain information from api call to JSON file to store in a list
        article_data_list = []

        for article in articles_list:
            
            abstract = article["abstract"]
            headline = article["headline"]["main"]
            lead_paragraph = article["lead_paragraph"]
            snippet = article["snippet"]
            article_link = article["web_url"]
            section_name = article["section_name"]
            pub_date = article["pub_date"]
            
            
            article_data_list.append({"Headline": headline,
                            "Abstract" : abstract,
                            "Lead Paragraph" : lead_paragraph,
                            "Snippet" : snippet, 
                            "URL" : article_link, 
                            "Date" : pub_date, 
                            "Section" : section_name})

        ## get images somehow
        return article_data_list

    except BaseException:
        return None