import streamlit as st

st.title("Welcome to Matteo Web")
st.header("Halo!")
st.subheader("Ini web yang keren")
st.write("Pencet tombol-tombol yang di bawah")
st.text("Tombolnya keren")
st.latex(r"E = mc^2")
st.latex(r"a^2 = b^2 = c^2")
st.latex(r"\frac{4}{2}=2")

button = st.button("Suprise Me")
button2 = st.button("Suprise Me Again")

if st.checkbox("Accept Terms and Condition"):
    st.write("OK")

if button:
    st.balloons()
    
if button2:
    st.snow()