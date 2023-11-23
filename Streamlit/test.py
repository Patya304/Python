import streamlit as st

bekeres1 = st.number_input(label="Adj meg egy számot")
 
bekeres2 = st.number_input(label="Adj meg egy másik számot")


menu = st.radio("Menu",
                ("Összeadas", "Kivonas", "Szorzas", "Osztas"))

ertek = 0

def calculate():
    if menu == "Összeadás":
        ertek = bekeres1 + bekeres2
    elif menu == "Kivonás":
        ertek = bekeres1 - bekeres2
    elif menu == "Szorzás":
        ertek = bekeres1 * bekeres2
    elif menu == "Osztás" and bekeres2!=0:
        ertek = bekeres1 / bekeres2
    else:
        st.warning("0-val nem osztunk")
        ertek = "?????"

      st.success(f"Valasz = {ertek}")
 
if st.button("Eredmény kiszámítása"):
    calculate()
