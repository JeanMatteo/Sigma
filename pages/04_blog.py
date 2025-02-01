import streamlit as st
st.title("This is a mini blog") 
with open('./pages/blog_files/School_Agenda.md','r') as f:
  content = f.read()
f.close()
st.markdown(content)
