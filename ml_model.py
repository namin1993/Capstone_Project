# Machine-Learning-Model
# Import Dependencies
import pandas as pd
import hvplot.pandas
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import db_connections

def agglomerativeClustering():

    #  Import and read the data from mongodb into dataframes
    terrorism_df = pd.DataFrame(list(db_connections.terrorism.find()))
    terrorism_df.drop(['_id'], axis=1, inplace=True)

    # Set Index
    terrorism_df.set_index('PERPETRATOR', inplace=True)

    # Remove un-useful columns
    terrorism_df = terrorism_df.drop(columns=['SUBREGION', 'DESCRIPTION', 'CITY'])

    # Drop n/a's
    df = terrorism_df.copy()
    df = df.dropna()

    # Create a new DataFrame that holds only the Date
    perpetrators_df = df.filter(items = ['DATE', 'STATE'])

    # Reformat any data in columns (type, split string, etc...)
    # Create latitude and longitude columns
    df[['latitude', 'longitude']] = df['COORDINATES'].str.split(',', 1, expand=True)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce').fillna(0).astype(int)
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce').fillna(0).astype(int)
    df = df.drop(columns='COORDINATES')

    # Drop the non-beneficial columns
    # Drop the 'DATE' and "STATE" column since it's not going to be used on the clustering algorithm.
    df = df.drop(columns=['DATE', 'STATE'])

    # Use get_dummies() to create variables for text features.
    X = pd.get_dummies(df,columns=['COUNTRY','REGION', 'CATEGORY'])
    print(X.shape)

    # Check any values for binning


    # Check the value plot density


    # Generate our categorical variable lists


    # Create a OneHotEncoder instance
    # enc = OneHotEncoder(sparse=False)


    # Fit and transform the OneHotEncoder using the categorical variable list


    #PCA-Analysis
    # Split our preprocessed data into our features and target arrays


    # Split the preprocessed data into a training and testing dataset


    # Create a StandardScaler instances
    scaler = StandardScaler()

    # Fit the StandardScaler
    X_scaled = scaler.fit_transform(X)

    # Using PCA to reduce dimensions to three principal components.
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(X_scaled)

    # Create a DataFrame with the three principal components.
    X_pca_df = pd.DataFrame(data=X_pca, columns=['PC 1', 'PC 2', 'PC 3'])
    X_pca_df.index = X.index

    # Find the best value for K
    inertia = []
    k = list(range(1, 11))

    # Calculate the inertia for the range of K values
    for i in k:
        km = KMeans(n_clusters=i, random_state=0)
        km.fit(X_pca_df)
        inertia.append(km.inertia_)

    # Create the elbow curve
    elbow_data = {"k": k, "inertia": inertia}
    df_elbow = pd.DataFrame(elbow_data)
    df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="Elbow Curve")

    # Initialize the K-means model
    agg = AgglomerativeClustering(n_clusters=4)

    # Fit the model
    model = agg.fit(X_pca_df)

    # Add the predicted class columns
    X_pca_df["class"] = model.labels_

    # Create a 3D-Scatter with the PCA data and the clusters
    fig = px.scatter_3d(X_pca_df,
                    x='PC 1',
                    y='PC 2',
                    z='PC 3',
                    color="class",
                    symbol="class",
                    width = 800,
                    )
    fig.update_layout(legend=dict(x=0, y=1))

    return fig
    # Scale the data


    # Instantiate the model


    # Fit and train the model


    # Predict the y_test


    # Create a summary of the model. Possibly return value for Flask app.


    # Return the graph figure. Possibly return value for Flask app.
