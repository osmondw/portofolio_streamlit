import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Portofolio", page_icon="star")
#dataframe initiation
df = pd.read_excel('data.xlsx', sheet_name='SC1')
df['checkout_date'] = pd.to_datetime(df['checkout_date'])
df['paid_date'] = pd.to_datetime(df['paid_date'])

# Calculate the duration of borrowing
df['duration'] = df['paid_date'] - df['checkout_date']

# Extract the duration in days, hours, minutes, and seconds
df['time'] = df['duration'].dt.days

# Print the data with the duration
duration = pd.DataFrame(df['time'].value_counts())
city = pd.DataFrame(df['city'].value_counts())
channel = pd.DataFrame(df['channel'].value_counts())
job = pd.DataFrame(df['occupation'].value_counts())
age = pd.DataFrame(df['age'].value_counts())
user = pd.DataFrame(df['user_id'].value_counts())

#city
city1 = city.index
city2 = city.values

#job
job1 = job.index
job2 = job.values

#age
age1 = age.index
age2 = age.values

colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige")

#header
st.header('Osmond Willyando')



#sidebar
with st.sidebar:
   selected=option_menu(
      menu_title="",
      options=[
         "Home",
         "Graph",
         "Portofolio",
         "Contact"
      ],
      icons=['house','bar-chart','gear','telephone'],
      default_index=0
   )

#define every state
#home
if selected=='Home':
   st.text('Anda di home')
#graph
if selected=='Graph':
   st.text('This graph is based on subscription sales data from one of the learning platforms')
   
   st.dataframe(df)
   tab1, tab2 =st.tabs(["Bar Graph", "Pie Chart"])

   with tab1:
      st.header("Showing Bar Graph")
      bar = st.selectbox("Buyers Based on ", ["Region", "Job"])
      
      if bar=='Region':
         chart_data = pd.DataFrame(np.random.randn(20, 4), columns=city1)
         st.bar_chart(chart_data)

      if bar=='Job':
         chart_data = pd.DataFrame(np.random.randn(20, 4), columns=job1)
         st.bar_chart(chart_data)
   with tab2:
      st.header("Showing Pie Chart")


#portofolio
if selected=='Portofolio':
   st.text('Menampilkan portofolio')
#contact
if selected=='Contact':
   st.text('Kontak saya di ')

