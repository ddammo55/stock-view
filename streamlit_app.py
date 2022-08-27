import streamlit as st
import pandas as pd
import plotly.express as px
view = [100,150,30]

st.write('# Hello World')
st.
sview = pd.Series(view)
sview

df = px.data.iris()
df["e"] = df["sepal_width"]/100
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", error_x="e", error_y="e")
fig.show()
