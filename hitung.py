import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("satuan awal", "C")
fx = st.text_input("satuan akhir", "R")
y = 0

if(sx=='C'):
  if(fx=='C'):
    x = y
  elif(fx=='R'):
      y = x*4/5 

st.write(x, ' ', sx, "=", y, fx)

