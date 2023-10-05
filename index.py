import  streamlit as st
from streamlit_option_menu import option_menu



def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

# with st.sidebar:
#    x=option_menu(
#       menu_title="Main Menu",
#       menu_icon='list-ul',
#       options=[
#          "Home",
#          "Graph",
#          "Portofolio",
#          "Contact"
#       ],
#       icons=['house','bar-chart','gear','telephone'],
#       default_index=0
#    )

selected_page = st.sidebar.option_menu("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()