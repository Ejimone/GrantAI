import streamlit as st
from lanchain_helper import generate_restaurant_name

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ["Italian", "Indian", "Chinese", "Mexican"])
# import the function tp get the history
# history = get_history()
# st.write("History", history)

if cuisine:
    response = generate_restaurant_name(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["food_items"].split(", ")

    st.write("Menu Items:")
    for item in menu_items:
        st.write("-", item)