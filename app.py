# Import Dependencies
from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
import pandas as pd
import json
import hvplot.pandas
import plotly
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import tensorflow as tf
import datetime as dt
#import scraping
import db_connections

app = Flask(__name__)
# Shows you what was scraped
@app.route("/")
def index():
    return render_template("index.html")

    #return render_template("index.html", str="Update News")
# Scrape updates in the database
# @app.route("/scrape")
# def scrape():
#    mars = mongo.db.mars
#    mars_data = scraping.scrape_all()
#    mars.update_one({}, {"$set":mars_data}, upsert=True)
#    return redirect('/', code=302)

# Question 1: Which organizations are responsible for the most deaths and injuries from 1972-2022?
@app.route('/chart1/')
def chart1():
    try:
        print("The mongodb connection worked!!")

        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)

        # Filter by date
        terrorism_df = terrorism_df[terrorism_df["DATE"] > '1971-12-31']

        # Group by 'PERPETRATOR' and sum up 'DEAD' and 'INJURED' numbers per PERPETRATOR
        q_1df = terrorism_df.groupby(['PERPETRATOR'])[['DEAD', 'INJURED']].sum().reset_index()
        q_1df['DEAD_AND_INJURED'] = q_1df['DEAD'] + q_1df['INJURED']
        q_1df.drop(columns=['DEAD', 'INJURED'], axis=1, inplace=True)

        # Sort values
        q_1df = q_1df.sort_values(['DEAD_AND_INJURED'], ascending=[False]).reset_index()

        # Create graph
        fig = px.bar(q_1df, x="DEAD_AND_INJURED", y="PERPETRATOR", 
                    color="PERPETRATOR", 
                    orientation='h', 
                    title='Total number of Dead and Injured caused by each Terrorist Group from 1972 - 2022', 
                    height=800)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)

    except Exception as e:
        print(f'{e}')

# Question 2: Which Countries have the most deaths and injuries from 1972-2022 from terrorism?
@app.route('/chart2/')
def chart2():
    try:
        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)

        # Filter by date
        terrorism_df = terrorism_df[terrorism_df["DATE"] > '1971-12-31']

        # Group by 'COUNTRY' and sum up 'DEAD' and 'INJURED' numbers per country
        q_2df = terrorism_df.groupby(['COUNTRY'])[['DEAD', 'INJURED']].sum().reset_index()

        # Sum up Dead and Injured. Drop 'DEAD' and 'INJURED' columns
        q_2df['DEAD_AND_INJURED'] = q_2df['DEAD'] + q_2df['INJURED']
        q_2df.drop(columns=['DEAD', 'INJURED'], axis=1, inplace=True)

        # Sort values
        q_2df = q_2df.sort_values(['DEAD_AND_INJURED'], ascending=[False]).reset_index(drop=True)

        # Create graph
        fig = px.bar(q_2df, x="DEAD_AND_INJURED", y="COUNTRY", 
            color="COUNTRY", 
            orientation='h', 
            title='Countries with the most Death and Injuries from Terrorism in 1972 - 2022', 
            height=3400)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)

    except Exception as e:
        print(f'{e}')

# Question 3: What are the most common categories of terrorism within each country from 1972-2022?
@app.route('/chart3/')
def chart3():
    try:
        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)
        q_3df = terrorism_df.groupby(['COUNTRY', 'CATEGORY'])[['CATEGORY']].count()

        return render_template("index.html", tables=[q_3df.to_html(classes='data', header="true")])

    except Exception as e:
        print(f'{e}')

# Question 4: On what particular decade were the most terrorist acts committed across the world?
@app.route('/chart4/')
def chart4():
    try:
        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)
        
        # Establish the bins.
        decade_bins = [0, 1969, 1979, 1989, 1999, 2009, 2019, 2029]
        group_names = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]

        # Filter by date
        terrorism_df = terrorism_df[terrorism_df["DATE"] > '1971-12-31']

        # Convert DATE column to datetime
        terrorism_df['incident_date'] = pd.to_datetime(terrorism_df['DATE'])

        # Categorize dates based on the bins.
        terrorism_df["YEAR"] = terrorism_df['incident_date'].dt.year
        decade_bins_dt = pd.to_datetime(decade_bins)
        terrorism_df["DECADE"] = pd.cut(terrorism_df["YEAR"], decade_bins_dt, labels=group_names)

        # Count the number of incidents per decade
        q_4df = terrorism_df.groupby(['DECADE'])[['DATE']].count().reset_index()

        # Create graph
        fig = px.bar(q_4df, x="DECADE", y="DATE", 
                    color="DECADE",  
                    title='Number of Terrorist acts per decade', 
                    height=800)

        fig.update_layout(
            xaxis_title="Decade",
            yaxis_title="Number of Incidents"
        )

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)

    except Exception as e:
        print(f'{e}')

# Question 5: World Map of all terrorist acts from 1972-2022
@app.route('/chart5/')
def chart6():
    try:
        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)

        # Filter by date
        terrorism_df = terrorism_df[terrorism_df["DATE"] > '1971-12-31']

        # Establish the bins.
        decade_bins = [0, 1969, 1979, 1989, 1999, 2009, 2019, 2029]
        group_names = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]

        # Convert DATE column to datetime
        terrorism_df['incident_date'] = pd.to_datetime(terrorism_df['DATE'])

        # Categorize dates based on the bins.
        terrorism_df["YEAR"] = terrorism_df['incident_date'].dt.year
        decade_bins_dt = pd.to_datetime(decade_bins)
        terrorism_df["DECADE"] = pd.cut(terrorism_df["YEAR"], decade_bins_dt, labels=group_names)

        # Create latitude and longitude columns
        terrorism_df[['latitude', 'longitude']] = terrorism_df['COORDINATES'].str.split(',', 1, expand=True)
        terrorism_df['latitude'] = pd.to_numeric(terrorism_df['latitude'], errors='coerce').fillna(0).astype(float)
        terrorism_df['longitude'] = pd.to_numeric(terrorism_df['longitude'], errors='coerce').fillna(0).astype(float)

        fig = px.scatter_mapbox(terrorism_df, lat="latitude", lon="longitude", hover_name="DATE", hover_data=["STATE", "PERPETRATOR"], 
                                color="DECADE", zoom=3, height=300)
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                },
                {
                    "sourcetype": "raster",
                    "sourceattribution": "Government of Canada",
                    "source": ["https://geo.weather.gc.ca/geomet/?"
                            "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                            "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
                }
            ])
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)

    except Exception as e:
        print(f'{e}')


@app.route('/chart6/')
def chart5():
    try:
        # Read terrorism dataframe
        terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
        terrorism_df.drop(['_id'], axis=1, inplace=True)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)

    except Exception as e:
        print(f'{e}')

if __name__ == "__main__":
   app.run()

