import pandas as pd
import plotly.express as px

df = px.data.stocks()
df.shape
df
px.line(df, x="date", y="GOOG")
