import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import FinanceDataReader as fdr

st.title('# Won Stock')

FAANG = ["FB", "AMZN", "AAPL", "NFLX", "GOOGL"]
faang_list = [fdr.DataReader(code, '2022', '2023')['Close'] for code in FAANG]
df_faang = pd.concat(faang_list, axis=1)
df_faang.columns = FAANG
df_ratio = df_faang / df_faang.iloc[0] - 1
df_ratio.columns.name = "company"
df = px.line(df_ratio, title="FAANG 일별 수익률")



st.plotly_chart(df, use_container_width=True)
