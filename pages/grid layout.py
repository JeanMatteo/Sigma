import streamlit as st

ncolumn = 6

columns = st.columns(ncolumn)

for i in range(ncolumn):     
    if i%ncolumn == 0:
        col = columns[0]
    if i%ncolumn == 1:
        col = columns[1]
    if i%ncolumn == 2:
        col = columns[2]
    if i%ncolumn == 3:
        col = columns[3]
    if i%ncolumn == 4:
        col = columns[4]
    if i%ncolumn == 5:
        col = columns[5] 

    with col:
      with st.container(border=True):
          st.write("Hello")
