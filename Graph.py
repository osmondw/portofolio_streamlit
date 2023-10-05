import streamlit as st
from streamlit_option_menu import option_menu

#sidebar
with st.sidebar:
   selected=option_menu(
      menu_title="Main Menu",
      menu_icon='list-ul',
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
#home
if selected=='Graph':
    st.text('Menampilkan grafik')
#home
if selected=='Portofolio':
    st.text('Menampilkan portofolio')
#home
if selected=='Contact':
    st.text('Kontak saya di ')

