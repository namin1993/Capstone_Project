# Database Connections
# Import Dependencies
from pymongo import MongoClient
import config

# Use MongoClient to set up mongodb connection
username = config.username
password = config.password
cluster = 'finalproject.1pamme7.mongodb.net'

cloudstr = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
mogodb_client = MongoClient(cloudstr)
db = mogodb_client['final_project']
terrorism = db["clean_terror_df"]