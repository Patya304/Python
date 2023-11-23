import streamlit as st

ertek = 0
adat1 = st.number_input("Kérek egy számot")
adat2 = st.number_input("Kérek még egy számot")

muveletek = st.radio("Menu",
                     ("ossze+","kivo-","szoro*", "oszt/"))

def szamologep():
  if muveletek == "ossze+":
    ertek = adat1 + adat2
  elif muveletek == "kivo-":
    ertek = adat1 - adat2
  elif muveletek == "szoro*":
    ertek = adat1 * adat2
  elif muveletek == "oszt/":
    ertek = adat1 / adat2
  else:
    st.warning("0-val nem osztunk")
  st.success(f"A valasz = {ertek}")

if st.button("Eredmény kiszámítása"):
    szamologep()
