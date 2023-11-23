import streamlit as st
 
st.title("Calculator")
 
# creates a horizontal line
st.write("---")

# adat1
num1 = st.number_input(label="Adj megy egy számot")
 
# adat2
num2 = st.number_input(label="Adj meg még egy számot")
