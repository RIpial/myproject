import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import matplotlib.pyplot as plt



header= st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()
interactive=st.container()

with header:
    st.title("JanataWifi!")

with dataset:
    st.header("Stock exchange Dataset")
    stock_data=pd.read_csv("stock_market_data.csv")
    st.write(stock_data.head())





with interactive:
    st.title('A closer look to the data')

    fig=go.Figure(data=go.Table(header=dict(values=list(stock_data[['date','trade_code','high','low','open','close','volume']].columns),
                                fill_color='#FFC0CB',
                                align='center'),
    cells=dict(values=[stock_data.date,stock_data.trade_code,stock_data.high,stock_data.low,stock_data.open,stock_data.close,stock_data.volume],
               fill_color='#FFFFFF',
               align='left')))
    fig.update_layout(margin=dict(l=5,r=5,b=10,t=10))
    st.write(fig)
    st.subheader('Line chart ')
    line_chart_data=stock_data.copy()





    date_cross_tab=pd.crosstab(line_chart_data['high'],line_chart_data['trade_code'])
    print(date_cross_tab)

    fig=px.line(date_cross_tab)
    st.write(fig)













