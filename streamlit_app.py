import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

st.title('# Won Stock')

df = px.data.stocks()
df = px.line(df, x="date", y="006620", title='동구바이오 차트')

st.plotly_chart(df, use_container_width=True)
