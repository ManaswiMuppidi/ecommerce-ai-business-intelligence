import streamlit as st
import pandas as pd
import plotly.express as px

st.title("E-Commerce AI Business Intelligence")
df=pd.read_csv("data/ecommerce_orders_large.csv")
c1,c2,c3=st.columns(3)
c1.metric("Revenue",f"${df.revenue.sum():,.0f}")
c2.metric("Profit",f"${df.profit.sum():,.0f}")
c3.metric("Orders",f"{len(df):,}")
summary=df.groupby("category",as_index=False)["revenue"].sum()
st.plotly_chart(px.bar(summary,x="category",y="revenue",title="Revenue by Category"),use_container_width=True)
