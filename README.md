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


## Project Deployment Instructions
    1.) Clone the github repository:
    git clone https://github.com/namin1993/Capstone_Project.git

    2.) Navigate to the directory through your terminal and create a virtual environment. 

    * Using Conda (you can create a virutal environment and install all packages in the requirements.txt file at the same time)
    ```conda create --name <virtualenv_name> --file requirements.txt
    conda activate <virtualenv_name>````

    * Using Python:
    ```virtualenv -p /usr/bin/python3.7.13 virtualenv_name
    source virtualenv_name/bin/activate
    pip install -r requirements.txt```

    3.) Run the application locally
    ```python app.py```

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

* Time management and Teamwork

    Time management and teamwork has been a huge factor in the completion of our project. Expectations of what a dashboard should look like versus the amount of time it actually took to realistically implement a feature was one contention in this application design. Priorities in implementing as many techniques in the project versus answering questions and parsing the data properly was also a major issue. The presentation also did not evenly space itself out between 2 minutes and 40 seconds for Raeann to show the full dashboard, as discussed in the group earlier. 
    
    Finally agreeing to the current dashboard design instead of a certain member copying some code and trying to switch everything to tableau the night before the presentation without communicating with the team was also an issue.

* Inserting properties to the GeoJSON file

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

* Heroku Deployment

    Originally, I received H10 errors from the deployment because certain modules were not included in the requirements.txt file. After fixing the requirements.txt file, I received H12 error codes. This may have been due to the number of API calls, number of databse connections,  Because of the deadline, a video recording of the dashboard was created. 


## Project Links

Google Slides:
https://docs.google.com/presentation/d/1Dv4_oMvHP1tcqSeELV1P3IkvWU_IuylzWD8664CBSYo/edit?usp=sharing

Dashboard Video Link:
https://drive.google.com/file/d/1oVcXEWrodwiwlcDvdibWVO_lmkHMKEuF/view?usp=sharing

