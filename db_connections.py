# Database Connections
# Import Dependencies
from pymongo import MongoClient
import config

# Use MongoClient to set up mongodb connection
username = config.username
password = config.password

'''
cluster = 'finalproject.1pamme7.mongodb.net'

#app.config["SECRET_KEY"]="3ab27fe2c90b101d9e7867c7f663b0ad15c0dbe0"
cloudstr = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
mogodb_client = MongoClient(cloudstr)
db = mogodb_client['final_project']
terrorism = db["clean_terror_df"]
'''

cluster = 'na-cluster-0.skgmjzn.mongodb.net'
cloudstr = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
mogodb_client = MongoClient(cloudstr)
db = mogodb_client['Final_Project']
terrorism = db["terrorism"]
countries = db["countries"]
gdp = db["GDP"]
gdp_growth = db["GDP_Growth_Rate"]
news = db["nyt_api"]