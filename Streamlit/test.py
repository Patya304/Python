import streamlit as st

ertek = 0
adat1 = st.number_input("Kérek egy számot")
adat2 = st.number_input("Kérek még egy számot")

muveletek = st.radio("Menu",
                     ("+","-","*", "/"))

def szamologep():
  if muveletek == "+":
    ertek = adat1 + adat2
  elif muveletek == "-":
    ertek = adat1 - adat2
  elif muveletek == "*":
    ertek = adat1 * adat2
  elif muveletek == "/":
    ertek = adat1 / adat2
  else:
    st.warning("0-val nem osztunk")
  st.success(f"A valasz = {ertek}")

if st.button("Eredmény kiszámítása"):
    calculate()
