# Machine-Learning-Model
# Import Dependencies
import pandas as pd
import hvplot.pandas
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import db_connections

#  Import and read the data from mongodb into dataframes
terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
terrorism_df.drop(['_id'], axis=1, inplace=True)

# Drop n/a's


# Reformat any data in columns (type, split string, etc...)


# Drop the non-beneficial columns


# Check any values for binning


# Check the value plot density


# Generate our categorical variable lists


# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)


# Fit and transform the OneHotEncoder using the categorical variable list


#PCA-Analysis
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
# Create the dendrogram
fig = ff.create_dendrogram(df_iris_pca, color_threshold=0)
fig.update_layout(width=800, height=500)
fig.show()

agg = AgglomerativeClustering(n_clusters=4)
model = agg.fit(df_iris_pca)