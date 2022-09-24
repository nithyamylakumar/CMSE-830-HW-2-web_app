import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

iris_df = sns.load_dataset('iris')

df = px.data.iris()
iris_df.head(10)
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length',symbol = 'species',title = 'IRIS DATASET 3D SCATTER PLOT REPRESENTATION')
fig
fig.show()

#plot 
st.plotly_chart(fig, use_container_width = True)