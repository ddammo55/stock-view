import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

df = px.data.stocks()
df = px.line(df, x="date", y="GOOG")

st.plotly_chart(df, use_container_width=True)
