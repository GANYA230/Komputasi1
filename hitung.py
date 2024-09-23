import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("satuan", "C")
st.write("Anda memasukkan", x, ' ',sx)

