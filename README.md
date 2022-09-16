# README
# Segment 4 (Full Review) September 10 - September 15

## Purpose and Overview:
The purpose of this analysis is to explore several questions regarding terroristic activity and to see whether there is a connection between country demographics, economic status, and military expenditures with terrorism in the last century. The completed analysis will be able to run locally on any computer and will contain interactive visualizations of the data including a map and web-scraped articles.

The reason this topic was selected was because it would enable us to work with large datasets full of information about many countries. Using these large datasets pertaining to country information and terrorism would allow us to use many techniques we learned throughout the course to transform the data as well as the flexibility to answer as many questions as possible. 

We also thought that the topic itself was interesting to look into and we wanted to make sure that the datasets would not be too limiting in case there was unexpected technical difficulty in answering certain questions listed in the next section.

Questions answered in this dashboard:  

 1.) Which organizations are responsible for the most deaths and injuries from 1972-2022?
    
 2.) Which states/regions of a country had the most terrorist attacks from 1972-2022?

 3.) What are the most common categories of terrorism within each region from 1972-2022?

 4.) On what particular decade where the most terroist acts committed across the world?

 5.) What is the demographic breakdown (gender ratio and percentage of each age range in a population) of each state where terrorism was committed?

## Machine Learning:
 An unsupervised machine learning model, agglomerative hierarchical clustering, is selected for grouping together clusters of terrorist attacks. We chose this machine-learning model in order to identify which attacks appeared to be similar to one another in outcome. This model will rely upon different columns of information merged from the "Terrorist" dataset.

 * Accuracy score:
	The PCA Variance Ratio is array([0.02212923, 0.01560112, 0.01320126]). This indicates a very low relationship between variables and clustering organization.

## Project Deployment Instructions
    1.) Clone the github repository:
    git clone https://github.com/namin1993/Capstone_Project.git

    2.) Navigate to the directory through your terminal and create a virtual environment. 

    * Using Conda (you can create a virutal environment and install all packages in the requirements.txt file at the same time)
    conda create --name <virtualenv_name> --file requirements.txt
    conda activate <virtualenv_name>

    * Using Python:
    virtualenv -p /usr/bin/python3.7.13 virtualenv_name
    source virtualenv_name/bin/activate
    pip install -r requirements.txt

    3.) Run the application locally
    python app.py

## Project Outline

### Week 1:
 * Assigning roles
 * Selecting a topic
 * Selecting Datasets
 * Creating project directory and code mock-up

### Week 2:
 * Confirming connection and data upload to the Cloud MongoDB
 * Cleaning data and adding collections on the database
 * Solving questions on the project (Creating a Plotly map)
 * Creating a working machine learning model
 * Selecting a dashboard template on the internet

### Week 3:
 * Competing the API
 * Creating the GeoJSON maps and trying to correct Flask routing
 * Working on the slide show presentation 
 * Working on the HTML/CSS file

### Week 4:
 * Finishing the slideshow presentation
 * Adding more features to the HTML/CSS code
 * Attempting heroku/git pages application deployment

## Project Challenges

* Time management and Teamwork:

    Time management and teamwork has been a huge factor in the completion of our project. Expectations of what a dashboard should look like versus the amount of time it actually took to realistically implement a feature was one contention in this application design. Priorities in implementing as many techniques in the project versus answering questions and parsing the data properly was also a major issue. The presentation also did not evenly space itself out between 2 minutes and 40 seconds for Raeann to show the full dashboard, as discussed in the group earlier. 
    
    Finally agreeing to the current dashboard design instead of a certain member copying some code and trying to switch everything to tableau the night before the presentation without communicating with the team was also an issue.

* Inserting properties to the GeoJSON file:

    Inserting certain gender and age statistics from a dataframe to the properties section in the GeoJSON file took about a full day to solve in order to bind the information on each country affected by terrorism on the map. This involved correctly converting the string JSON to an JSON object that was iterable and correctly matching certain keys to certain values as noted in the code.

* Creating a virtual environment:

    On creating the new conda virtual environment with a requirements.txt file from scratch, I ran into a problem where some of the packages:

    - keras[version='==2.9.0']
    - path[version='==16.4.0']
    - numpydoc[version='==1.21.5']
    - websockets[version='==10.1']
    - imbalanced-learn[version='==0.9.0']

    were unable to be found by conda's package manager because the it was not unable to find it on certain channels that it was pre-programmed to search through.
    In order to correct this, I ran the command on my terminal:

    conda config --append channels conda-forge

    and removed version control from the following packages:
    - numpydoc (originally supposed to be version 1.21.5)
    - async-timeout (originally supposed to be version 0.13.0)

    I don't think this would have been a problem if certain packages were uploaded seperately by using "pip install" instead of including them in the requirements.txt, but it's something to keep in mind.

* Finding supplementary datasets:

    It would have been ideal to have found more datasets pertaining to GDP, military expenditure, gender ratio, and poverty rates in all countries and the relationship between that and the number of terrorist attacks affecting the country.
    
    However, there often was no data or not enough data to be found for certain countries around certain decades. We did not want to apply data from 2022 to all years starting from 1972 since it would not be an accurate representation of the state of the country when the terrorist attack occurred.

* Heroku Deployment:

    Originally, I received H10 errors from the deployment because certain modules were not included in the requirements.txt file. After fixing the requirements.txt file, I received H12 error codes. This may have been due to the number of API calls, number of databse connections,  Because of the deadline, a video recording of the dashboard was created. 


## Dashboard Images

### Top of Dashboard
![Top of Dashboard]()

### Bottom of Dashboard
![Bottom of Dashboard]()

### Bar Graph
![Bar Graph]()

### Plotly Map
![Plotly Map]()

### GeoJSON Map
![GeoJSON Map]()

## Project Links

Google Slides:
https://docs.google.com/presentation/d/1Dv4_oMvHP1tcqSeELV1P3IkvWU_IuylzWD8664CBSYo/edit?usp=sharing

Dashboard Video Link:
https://drive.google.com/file/d/1oVcXEWrodwiwlcDvdibWVO_lmkHMKEuF/view?usp=sharing


# Previous Segments from August 15 - September 9
# Segment 3

## Machine Learning:
* Machine Learning Model choice:
    * An unsupervised machine learning model, agglomerative hierarchical clustering, is selected for grouping together clusters of terrorist attacks. We chose this machine-learning model in order to identify which attacks appeared to be similar to one another in outcome. This model will rely upon different columns of information merged from the "CIA-Countries" dataset and "Terrorist" dataset 

* Preliminary data preprocessing:
    * Dataframes from several datasets will be pre-processed by dropping non-beneficial columns, splitting the 'COORDINATES' column into 'longitude' and 'latitude', creating dummies for certain features, and checking for any values for binning.

    Features will be then be split between 2 dataframes, one for information that will remain categorical and one which will be filled with integers for PCA analysis.

* Preliminary feature engineering and preliminary feature selection, including their decision-making process
    * Although we are not making any predictions from our machine learning model, it would be possible to calculate the average amount of time passed between  each terrorist within a given country/region from 1972-2022. Our model will heavily depend on feature selection, which will rely mainly on intuition and PCA analysis for further feature reduction.

* Is data split into training and testing sets?
    * Data does not need to be split between training and testing sets under the agglomerative hierarchical clustering model. We cannot make predictions about the next terrorist attack or categorize each terrorist attack or country in any way from the datasets. 
    
* Changes to machine learning model:
    * We will merge terrorism data with age, gender, and/or GDP (PPP) columns for more data for hierarchical analysis.

* Accuracy score:
	The PCA Variance Ratio is array([0.02212923, 0.01560112, 0.01320126]).  Very low relationship between variables and clustering organization.

![Machine Learning Code](https://github.com/namin1993/Capstone_Project/blob/7d0fbf01431cebec3116a9605fb66d21f0f03bd5/Dashbaord%20Images/Machine_Learning_Graph.png)

## Database Management:

Since this segment did not require deliverables for database management, other deliverables are discussed here.

## Presentation:
* I expanded upon the rough draft presentation created last week.
* The new format and structure provides an outline of the final presentation and indicates where we need to add material for the presentation to be complete.  It will continue to be refined this week, prior to the final class.
* For ease of use, the working draft is constructed in [PowerPoint](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment%203%20presentation%20drafts/final_presentation_v2.pptx).  The completed version will be submitted in the Google Slides format requested by the Module.  The current rough draft version is on [Google Slides](https://docs.google.com/presentation/d/1E_kpYPFL0a_KAIhd9gufZIozvmDTO1Q2R3JtpMvM-yI/edit?usp=sharing) as well.  
* I also created a ["style guide"](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment%203%20presentation%20drafts/dashboard_style_guide.pptx) as a companion to the presentation.  The "style guide" assists in developing the dashboard so that there is a visual harmony between the presentation and the dashboard.  This will provide a nice effect since we are demonstrating our dashboard during our in-class presentation.

## Dashboard Work:
### Plots:
* In addition the above, I have created plots from our [databases](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment_3_DB_charts/charts_terror.ipynb).  The goal is to provide our team with many resources so that we can edit our choices for the final dashboard to include only the best representations of data.  

Examples are pictured below.  
![bar and code](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/lauren_resources_segment_3/bar%20and%20code.png)

![pie and bar](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/lauren_resources_segment_3/pie%20and%20bar.png)

### Sortable Table:
* First, I [re-cut the terror_df](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment_3_load_terror_table/terror_data_table_mod.ipynb) to include the null fields, which I previously dropped, to determine whether that data should be included in the sortable table.

* Next, I reformatted the code used for the Module 11 to create an [app file](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment_3_load_terror_table/static/js/app.js) for our dashboard. 

* The [HTML](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/segment_3_load_terror_table/index.html) from Module 11 was similarly repurposed.  Another teammate is creating the skeleton of the dashboard, so I only changed HTML code where it concerns the new table so that she can copy it and paste it into the completed skeleton.

Examples of the updated HTML code are pictured below.  The Module 11 code is on the left and the new code on the right.
![HTML](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/lauren_resources_segment_3/script.png)
![HTML headers](https://github.com/namin1993/Capstone_Project/blob/sement_3_lauren/lauren_resources_segment_3/headers.png)




# Segment 2:

## Machine Learning:

* Machine Learning Model choice:
    * An unsupervised machine learning model, agglomerative hierarchical clustering, is selected for grouping together clusters of terrorist attacks. We chose this machine-learning model in order to identify which attacks appeared to be similar to one another in outcome. This model will rely upon different columns of information merged from the "CIA-Countries" dataset and "Terrorist" dataset 

* Preliminary data preprocessing:
    * Dataframes from several datasets will be pre-processed by dropping non-beneficial columns, splitting the 'COORDINATES' column into 'longitude' and 'latitude', creating dummies for certain features, and checking for any values for binning.

    Features will be then be split between 2 dataframes, one for information that will remain categorical and one which will be filled with integers for PCA analysis.

* Preliminary feature engineering and preliminary feature selection, including their decision-making process
    * Although we are not making any predictions from our machine learning model, it would be possible to calculate the average amount of time passed between  each terrorist within a given country/region from 1972-2022. Our model will heavily depend on feature selection, which will rely mainly on intuition and PCA analysis for further feature reduction.

* Is data split into training and testing sets?
    * Data does not need to be split between training and testing sets under the agglomerative hierarchical clustering model. We cannot make predictions about the next terrorist attack or categorize each terrorist attack or country in any way from the datasets. 

## Database Management

### [Cleaning Terror Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/cleaning_terror_df.ipynb): 

* First, I examined the CSV to ascertain the format of the data and formulate a gameplan for cleaning.  Next, I loaded the CSV into the notebook and continued examining the data.  Functions like ".head()"and ".dtypes" are useful to understand the structure.
![head and dyptes](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/head%20and%20dytpes.png)

* Using a loop to identify null values is also a helpful tactic to obtain information on the dataset.
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


### [Cleaning CIA Data Frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_v5.ipynb):

* Many of the examination steps noted above were repeated [here](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_df_explore.ipynb). However, because this data set is considerably larger than the previous data set, I searched for columns likely to provide data to answer the questions posed in Segment 1.  This process reduced over 1100 columns to about 50 columns.

* Since I knew the pertinent columns,  I only loaded those columns into the notebook.
![column example]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/cia%20column%20names.png)

* As a strategy, I loaded the data as “string” data type because I anticipated using slicing as a method to retain necessary data and remove unwanted data.
![string]( https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/lauren_resources_week_2/loaded%20as%20string.png)

* Next, I used the [exploartory notebook](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/clean_cia_df_explore.ipynb) to determine how to slice the strings.

* In order to balance multiple priorities, I focused on creating a “[rough draft](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_data_clean/first_pass_clean_cia.csv)” data frame so my groupmates could access and begin to work with the data.

* The final data frame will be uploaded as collection to Mongo.  

### [Join Data Frames](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_join_lang_relig.ipynb)

* The final data frame is comprised of 3 dataframes.

* First, the [Languages data frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_language.ipynb) and the [Religions data frame](https://github.com/namin1993/Capstone_Project/blob/Lauren_week_2/segment_2_join_dfs/cia_religion.ipynb) were cut from the CIA dataframe.  

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

## Dashboard Design

A free HTML/CSS template theme from possibly this source: https://themewagon.com/themes/celestial-free-responsive-bootstrap-4-admin-dashboard-template/

will be used to organize our graphs and maps of our dashboard application. We decided that the theme has to use Bootstrap4 as a framework for template layout. This was so that when we edit the dashboard html template in anyway, it will be easier to troubleshoot any issues by referring to Bootstrap4 resource material.

Given the size of some of our graphs, our dashboard will provide links to each chart, causing the webpage to reload. This might compomise on the loading speed of the webpage. This however, is done because we can't nest multiple functions in a single flask route. For a dahboard application built on Flask, you cannot make a set of functions available for a particular route, you can only define the one specific thing that the server will do when that route is called. 

The application design may change later on, however, depending on what the group agrees to for a better layout of information and/or a better way to create an application layout which does not slowdown the webpage's loading time.

![Dashboard_Men](https://github.com/namin1993/Capstone_Project/blob/a61ac5e1be810cc29df96e6e34b1bf62f2ee9544/Dashbaord%20Images/Dashboard_1.png)
![Dashboard_Map](https://github.com/namin1993/Capstone_Project/blob/a61ac5e1be810cc29df96e6e34b1bf62f2ee9544/Dashbaord%20Images/Dashboard_2.png)
![Dashboard_Graph](https://github.com/namin1993/Capstone_Project/blob/a61ac5e1be810cc29df96e6e34b1bf62f2ee9544/Dashbaord%20Images/Dashboard_3.png))

### Rough Draft of Slide Presentation:
https://docs.google.com/presentation/d/1Fzlg9L7P3iCK86b989-ztdstdTh77HLjKwNlnZTFXi8/edit?usp=sharing


