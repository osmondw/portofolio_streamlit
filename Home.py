import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import calendar


st.set_page_config(page_title="Portofolio", page_icon="star")
#dataframe initiation
df = pd.read_excel('Data Analyst Test.xlsx', sheet_name='Superstore')
# df = df.drop(df.index[0])
# make the new header with the first row 
new_header = df.iloc[0] #take the first row
df = df[1:] #using data from the second row
df.columns = new_header # set header with the first row

# Calculation
# dom = df['Domisili'].value_counts()
# cat = df['Category'].value_counts()
# df_filtered = df.groupby('Bahasa').sum()
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
   # Convert "Tanggal Daftar" to datetime
   # Sample DataFrame with a "Tanggal Daftar" column
   
   
   # st.write(Dom)
   # tab1, tab2 =st.tabs(["Bar Graph", "Pie Chart"])

   # col1, col2, col3 = st.columns(3)
   
   # with tab1:
   st.header("Showing Bar Graph")
   # bar = st.selectbox("Buyers Based on", ["Region", "Job","Language"])

   # if bar=='Region':
   #    # Count the occurrences of each city
   #    city_counts = df['Domisili'].value_counts()
   #    # Create a DataFrame from the city counts
   #    city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
   #    # Create a bar chart in Streamlit
   #    st.bar_chart(city_df.set_index('Domisili'))

   # if bar=='Job':
   #    # Count the occurrences of each city
   #    job_counts = df['Pekerjaan'].value_counts()
   #    # Create a DataFrame from the city counts
   #    job_df = pd.DataFrame({'Job': job_counts.index, 'Count': job_counts.values})
   #    # Create a bar chart in Streamlit
   #    st.bar_chart(job_df.set_index('Job'))
      
   # if bar=='Language':
   #    # Count the occurrences of each city
   #    lang_counts = df['Bahasa'].value_counts()
   #    # Create a DataFrame from the city counts
   #    lang_df = pd.DataFrame({'Language': lang_counts.index, 'Count': lang_counts.values})
   #    # Create a bar chart in Streamlit
   #    st.bar_chart(lang_df.set_index('Language'))
   
   bar = st.selectbox("Buyers of each language", ["ALL","ENGLISH", "MANDARIN","JEPANG","FRENCH","KOREA"])

   if bar=='ALL':
      # Line chart sales
      # Convert "Tanggal Daftar" to datetime
      df['Tanggal Daftar'] = pd.to_datetime(df['Tanggal Daftar'])
      # Extract year and month
      df['Year'] = df['Tanggal Daftar'].dt.year
      df['Month'] = df['Tanggal Daftar'].dt.month
      # Group by year and month, and count the number of entries
      monthly_counts = df.groupby(['Year', 'Month']).size().reset_index(name='Count')

      # Create a pivot table to ensure all months are included
      pivot_monthly_counts = monthly_counts.pivot(index='Month', columns='Year', values='Count').fillna(0)

      # Rename the index to month names and sort by month
      month_names = [calendar.month_name[i] for i in range(1, 13)]
      pivot_monthly_counts.index = month_names

      # Sort the index based on month order
      month_order = [calendar.month_name[i] for i in range(1, 13)]
      pivot_monthly_counts = pivot_monthly_counts.reindex(month_names, axis=0)
      # Create a Streamlit line chart
      st.line_chart(pivot_monthly_counts, use_container_width=True)

      st.write(month_names)
      st.write(month_order)
      #based on city
      # Count the occurrences of each city
      city_counts = df['Domisili'].value_counts()
      # Create a DataFrame from the city counts
      city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(city_df.set_index('Domisili'))

      #based on category
      # Count the occurrences of each city
      cat_counts = df['Category'].value_counts()
      # Create a DataFrame from the city counts
      cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(cat_df.set_index('Category'))   

   if bar=='ENGLISH':
      df2 = df.loc[df['Bahasa'] == 'ENGLISH']
      col1, col2 = st.columns(2)
      
      with col1:
         #based on city
         
         # Count the occurrences of each city
         city_counts = df2['Domisili'].value_counts()
         # Create a DataFrame from the city counts
         city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
         # Create a bar chart in Streamlit
         st.bar_chart(city_df.set_index('Domisili'))

      with col2:
         #based on category
         # Count the occurrences of each city
         cat_counts = df2['Category'].value_counts()
         # Create a DataFrame from the city counts
         cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
         # Create a bar chart in Streamlit
         st.bar_chart(cat_df.set_index('Category'))

   if bar=='MANDARIN':
      
      df2 = df.loc[df['Bahasa'] == 'MANDARIN']
      #based on city
      # Count the occurrences of each city
      city_counts = df2['Domisili'].value_counts()
      # Create a DataFrame from the city counts
      city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(city_df.set_index('Domisili'))

      #based on category
      # Count the occurrences of each city
      cat_counts = df2['Category'].value_counts()
      # Create a DataFrame from the city counts
      cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(cat_df.set_index('Category'))

   if bar=='JEPANG':
      df2 = df.loc[df['Bahasa'] == 'JEPANG']
      #based on city
      
      # Count the occurrences of each city
      city_counts = df2['Domisili'].value_counts()
      # Create a DataFrame from the city counts
      city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(city_df.set_index('Domisili'))

      #based on category
      # Count the occurrences of each city
      cat_counts = df2['Category'].value_counts()
      # Create a DataFrame from the city counts
      cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(cat_df.set_index('Category'))

   if bar=='FRENCH':
      df2 = df.loc[df['Bahasa'] == 'FRENCH']
      #based on city
      
      # Count the occurrences of each city
      city_counts = df2['Domisili'].value_counts()
      # city_counts = city_counts.sort_values(ascending=False)
      # Create a DataFrame from the city counts
      city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
      # city_df = city_df.sort_values(by='Count', ascending=False)

      # Create a bar chart in Streamlit
      st.bar_chart(city_df.set_index('Domisili'))

      #based on category
      # Count the occurrences of each city
      cat_counts = df2['Category'].value_counts()
      # Create a DataFrame from the city counts
      cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(cat_df.set_index('Category'))

   if bar=='KOREA':
      df2 = df.loc[df['Bahasa'] == 'KOREA']
      #based on city
      
      # Count the occurrences of each city
      city_counts = df2['Domisili'].value_counts()
      # Create a DataFrame from the city counts
      city_df = pd.DataFrame({'Domisili': city_counts.index, 'Count': city_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(city_df.set_index('Domisili'))

      #based on category
      # Count the occurrences of each city
      cat_counts = df2['Category'].value_counts()
      # Create a DataFrame from the city counts
      cat_df = pd.DataFrame({'Category': cat_counts.index, 'Count': cat_counts.values})
      # Create a bar chart in Streamlit
      st.bar_chart(cat_df.set_index('Category'))

#portofolio
if selected=='Portofolio':
   st.text('Menampilkan portofolio')
#contact
if selected=='Contact':
   st.text('Kontak saya di ')

