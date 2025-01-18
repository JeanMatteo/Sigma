import streamlit as st
import os

col1,col2,col3 = st.columns(3)
with col1:
    st.image(r'./images/Earth.png')
with col2:
    st.image(r'./images/microsoft_teams.png')
with col3:
    st.image(r'./images/thonny-logo.png')
    
folder = os.listdir('images')
st.write(folder)

col1, col2 = st.columns(2)
with col1:
    selection = st.selectbox("Choose the picture",options = folder)

with col2:
    st.image(r'./images/'+ selection)


