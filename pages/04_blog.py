import streamlit as st
st.title("This is a mini blog") 
with open('./pages/blog_files/first_blog.md','r') as f:
  content = f.read()
f.close()
st.markdown(content)
