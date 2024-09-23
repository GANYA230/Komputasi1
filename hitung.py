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
  elif(fx=='F'):
    y = (x+32)*5/9
  elif(fx=='K'):
    y = x + 273
elif(sx=='R'):
  if(fx=='C'):
    y = x*5/4
  elif(fx=='R'):
    x = y 
  elif(fx=='F'):
    y = (x+32)*4/9
  elif(fx=='K'):
    y = x*5/4+273
elif(sx=='F'):
  if(fx=='C'):
    y = (x-32)*5/9
  elif(fx=='R'):
    x = (x-32)*4/9
  elif(fx=='F'):
    x = y
  elif(fx=='K'):
    y = ((x-32)*5/9)+273
elif(sx=='K'):
  if(fx=='C'):
    y = x-273
  elif(fx=='R'):
    x = (x-273)*4/5
  elif(fx=='F'):
    x = (x-273)*9/5+32
  elif(fx=='K'):
    x = y

st.write(x, ' ', sx, "=", y, fx)

