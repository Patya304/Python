import streamlit as st

bekeres1 = st.number_input(label="Szam1")
bekeres2 = st.numoer_input(label="szam2")


menu = st.radio("Menu",
                ("Összeadas", "Kivonas", "Szorzas", "Osztas"))
