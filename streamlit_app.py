import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

st.title('# Won Stock')

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

item_code = "326030"
item_name = "SK바이오팜"
page_no = 1

# 종목 URL 만들기
url = f"https://finance.naver.com/item/sise_day.nhn?code={item_code}&page={page_no}"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

html = bs(response.text, "lxml")
table = html.select("table")
len(table)
temp = table[0].dropna()
st.temp
