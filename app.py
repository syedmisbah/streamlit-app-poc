import streamlit as st
import datetime as dt
import requests
import pandas as pd
import json
import os 
import json

import pandas as pd
from flask import Flask, jsonify, request
from prophet.serialize import model_from_json, model_to_json

# dt.datetime.strptime('2021-07-24',format='')
min_date = dt.datetime.fromisoformat('2021-07-24')
max_date = dt.datetime.fromisoformat('2021-07-31')

st.image("logo.jpg")
st.title('SWVL Forecasting Control Center')

selected_fx = st.sidebar.radio(options=['Train','Predict'],label = 'Choose option')

if selected_fx=='Train':
    st.text(1)
else:

    st.markdown("""Please input the dates for which you want to forecast. You can either choose to upload a csv file with the dates or select start and end dates from the date picker.""")

    if st.radio(options=['Next 7 days','Select Dates'],label='Choose')=='Upload File':
            response = requests.post('http://127.0.0.1:5000/v0/model/predict')
            json_res = json.loads(response.json())
            df_res = pd.DataFrame.from_dict(json_res)
            st.write(df_res)
    else:
        date_from_input = st.date_input(label='Select from date',min_value=min_date,max_value=max_date)
        date_to_input = st.date_input(label='Select to date',min_value=min_date,max_value=max_date)

        if(st.button(label='Predict'))==True:
            response = requests.post('http://127.0.0.1:5000/v0/model/predict')
            json_res = json.loads(response.json())
            df_res = pd.DataFrame.from_dict(json_res)
            st.write(df_res)
