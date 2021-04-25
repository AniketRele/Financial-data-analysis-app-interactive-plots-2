import streamlit as st
import pandas as pd
from chart_studio import plotly
import plotly.express as px

@st.cache
def load_data():
    data=pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\Output.csv")
    return data
def gold():
    gold = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\gold.csv")
    return gold
def bitcoin():
    bitcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\bitcoin.csv")
    return bitcoin
def litcoin():
    litcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\litcoin.csv")
    return litcoin
def eth():
    eth = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\etherium.csv")
    return eth
def dollar():
    dollar = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\dollar.csv")
    return dollar
def sap500():
    sap500 = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\S&P500.csv")
    return sap500

st. set_page_config(layout="wide")
st.title('US Bitcoin Market Analysis- Bitcoin, Litcoin & Etherium')

fig_go4 = px.line(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','High_Bitcoin','High_Litcoin','High_Etherium','Low_Gold','High_Gold','Low_dollar','High_dollar','Low_sap500','High_sap500'],
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
fig_go4.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig_bit = px.scatter_matrix(bitcoin())
fig_lit = px.scatter_matrix(litcoin())
fig_eth = px.scatter_matrix(eth())
fig_go = px.scatter_matrix(gold())
fig_do = px.scatter_matrix(dollar())
fig_sap = px.scatter_matrix(sap500())

st.subheader('Comparison(contd.) and Pairplots for Individual currencies are given below which shows feature vs. feature plot.')
st.header('Comparison of Low and High for Gold,Dollar and S&P500 with the Digital Currencies')
st.plotly_chart(fig_go4, use_container_width=True)
st.header('Featurewise comparison plot for Bitcoin')
st.plotly_chart(fig_bit, use_container_width=True)
st.header('Featurewise comparison plot for Litcoin')
st.plotly_chart(fig_lit, use_container_width=True)
st.header('Featurewise comparison plot for Etherium')
st.plotly_chart(fig_eth, use_container_width=True)
st.header('Featurewise comparison plot for Gold')
st.plotly_chart(fig_go, use_container_width=True)
st.header('Featurewise comparison plot for Dollar')
st.plotly_chart(fig_do, use_container_width=True)
st.header('Featurewise comparison plot for S&P500')
st.plotly_chart(fig_sap, use_container_width=True)
st.subheader('The above pairplots shows how each feature is related to the other for the currencies given above.')