import streamlit as st
 
st.title("Calculator")
 
# creates a horizontal line
st.write("---")

# adat1
num1 = st.number_input(label="Adj megy egy számot")
 
# adat2
num2 = st.number_input(label="Adj meg még egy számot")


st.write("Operátor")
 
operation = st.radio("Menü:",
                    ("Összeadás", "Kivonás", "Szorzás", "Osztás")

ans = 0
 
def calculate():
    if operation == "Összeadás":
        ans = num1 + num2
    elif operation == "Kivonás":
        ans = num1 - num2
    elif operation == "Szorzás":
        ans = num1 * num2
    elif operation=="Osztás" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("0-val való osztás hibája. Adjon meg egy nem nulla számot.")
        ans = "Nem definiálható "
 
    st.success(f"Megoldás = {ans}")
