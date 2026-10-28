import streamlit as st
from cleaning_data import load_clean_data
from customer_analysis import customer_analysis
from orders_analysis import analyze_order,monthly_orders
from delivery_analysis import analyze_delivery,delivery_status
import os
from connect_sql import connect_database

st.set_page_config(page_title="Food Delivery Analysis 🍕",layout="wide")

st.title("Food Delivery Analysis App 🍕")

try:
    data=load_clean_data()
    customer=data['Customers']
    orders=data['Orders']
    menu=data['Menu']
    rest=data['Rest']
    delivery=data['Delivery']
    print("All Table Loaded")
except:
    print("Database connection Failed")


CA,OA,DA=st.tabs(['Customer Analysis','Order Analysis','Delivery Analysis'])

with CA:
    st.header("Customer Analysis Report")
    st.divider()
    col1,col2,col3=st.columns(3)
    customer_analysis_data=customer_analysis(customer,orders)    
    col1.header("Total Customer")
    col1.subheader(customer_analysis_data['Total_customers'])
    col2.header("Repeted Customers")
    col2.subheader(customer_analysis_data['repeted_custumers'])
    col3.header("New Customers")
    col3.subheader(customer_analysis_data['new customers'])
    st.divider()
    st.header("Gender Analysis")
    st.divider()
    st.bar_chart(customer_analysis_data['Gender count'])
    st.divider()
    st.header("Area Analysis")
    st.divider()
    st.bar_chart(customer_analysis_data['city count'])
with OA: 
    st.header("Order Analysis Report")
    orders_analysis_data=analyze_order(orders)
    st.divider()
    col1,col2,col3=st.columns(3)
    col1.header("Total Revenue")
    col1.subheader(orders_analysis_data['Revenue'])
    col2.header("Total Orders")
    col2.subheader(orders_analysis_data['Total_Orders'])
    col3.header("Average Order Value")
    col3.subheader(orders_analysis_data['Average Order Value'])
    st.divider()
    monthly_order_data=monthly_orders(orders)
    st.header("Monthly Order Analysis")
    st.divider()
    st.line_chart(monthly_order_data)
    
with DA:
    st.header("Delivery Analysis Report 🚗")
    st.divider()
    d_m=analyze_delivery(orders,delivery)['delivery_minutes']
    average_delivery_minutes=d_m.mean()
    st.header("Average delivery time")
    st.subheader(average_delivery_minutes)
    #st.metric("Average delivery time","%.1f"%average_delivery_minutes)
    st.divider()
    st.header("Delivery Staus")
    status=delivery_status(delivery)
    st.bar_chart(status)
    st.divider()
    st.subheader("Delivery Data Record")
    st.dataframe(analyze_delivery(orders,delivery))
st.sidebar.header("Food Delivery Database")

engine=connect_database()

if engine is not None:
    st.sidebar.subheader("Status : 🟢connected")
else:
    st.sidebar.subheader("Status : 🔴Not connected")




    






