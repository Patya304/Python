import streamlit as st
 
st.title("Calculator App using Streamlit")
 
# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Adj meg egy számot")
 
# input 2
num2 = st.number_input(label="Adj meg egy másik számot")
 
st.write("Operation")
 
operation = st.radio("Menu:",
                    ("Összeadás", "Kivonás", "Szorzás", "Osztás"))
 
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
        st.warning("0-val nem osztunk")
        ans = "?????"
 
    st.success(f"Valasz = {ans}")
 
if st.button("Eredmény kiszámítása"):
    calculate()
