## Import Dependencies
from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
from urllib.parse import quote_plus
#import scraping

app = Flask(__name__)

# Use MongoClient to set up mongodb connection
username = quote_plus('namin')
password = quote_plus('passMONG1446%23%23')
cluster = 'na-cluster-0.skgmjzn.mongodb.net'

app.config["SECRET_KEY"]="3ab27fe2c90b101d9e7867c7f663b0ad15c0dbe0"
cloudstr = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
#app.config["MONGO_URI"] = cloudstr

#mogodb_client = PyMongo(app)
mogodb_client = MongoClient(cloudstr)
db = mogodb_client.test

# Shows you what was scraped
@app.route("/")
def index():
    try:
        #mars = mongo.db.mars.find_one()
        print("The mongodb connection worked!!")
        return render_template("index.html", str="Hello World")
    except Exception as e:
        print(f'{e}')

# Scrape updates in the database
# @app.route("/scrape")
# def scrape():
#    mars = mongo.db.mars
#    mars_data = scraping.scrape_all()
#    mars.update_one({}, {"$set":mars_data}, upsert=True)
#    return redirect('/', code=302)

if __name__ == "__main__":
   app.run()

