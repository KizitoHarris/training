# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:37:18 2025

@author: HarrisKizito
"""

import streamlit as st
import pandas as pd
import numpy as np
import Functions as fx


st.subheader("My data cleaning app")

file = st.file_uploader("Select a file", type ='xlsx')

if file is not None:

    data = pd.read_excel(file)
    
    df = fx.Clean(data)
    
    st.write(df.shape)
    st.write(df.head())
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        #show loan amount
        amount = df["Loan_amount"].sum()
        st.metric("the loan amount is:", amount)
    
    with col2:
        #show number of loans
        number = df["Borrower_ID"].count()
        st.metric("the number of loans is:", number)
    
    with col3:
        #show number of youths
        mask = df["Age"]<=35
        youths = df[mask]['Borrower_ID'].count()
        st.metric("the number of youths is: ", youths)
    
    with col1:
        #show number of women
        mask = df["Gender"] == "Female"
        women = df[mask]['Borrower_ID'].count()
        st.metric("the number of women is:", women)
    
    with col2:
        #show number of young women
        mask = (df["Gender"] == "Female") & (df["Age"]<=35)
        young_women = df[mask]['Borrower_ID'].count()
        st.metric("the number of young women is:", young_women)
    
    with col3:
        #show interest rate
        interest =round (df["Interest_rate"].mean(),2)
        st.metric("the average interst is:", interest)
        
    df.to_excel("data.xlsx", index = False)
    
    #Add button to down load data
    st.download_button(
        label = "Click to download data",
        data = df.to_csv(index = False), #convert dataFrame to excel data
        file_name ="Clean data.xlsx",
    )







