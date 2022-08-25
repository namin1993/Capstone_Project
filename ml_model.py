# Machine-Learning-Model
# Import Dependencies
import pandas as pd
import hvplot.pandas
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import tensorflow as tf


#  Import and read the data from mongodb into dataframes


# Drop n/a's


# Reformat any data in columns (type, split string, etc...)


# Drop the non-beneficial columns


# Check any values for binning


# Check the value plot density


# Generate our categorical variable lists


# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)


# Fit and transform the OneHotEncoder using the categorical variable list


# Split our preprocessed data into our features and target arrays


# Split the preprocessed data into a training and testing dataset


# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler


# Scale the data


# Instantiate the model


# Fit and train the model


# Predict the y_test


# Create a summary of the model. Possibly return value for Flask app.


# Return the graph figure. Possibly return value for Flask app.