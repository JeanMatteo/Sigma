import streamlit as st
import os

files = os.listdir('./pages/blog_files') 

for each_file in files:
  with st.container(border=True):
    with open('./pages/blog_files/' + each_file,'r') as f:
      content = f.read()
    f.close()
    st.markdown(content)
