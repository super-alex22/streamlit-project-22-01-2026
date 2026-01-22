import streamlit as st
st.title("Login system")
name = st.text_input("Enter name")
age = st.number_input("Enter age")
if st.button("Check"):
  if age<18 and name=="":
    st.error("You are not of legal age to use this program")
  if name.strip()=="":
    st.warning("I'd like to kindly have you asked to enter text")
  elif not name.isalpha():
    st.warning("Warning")
  else:
    st.success("The text has been entered correctly")
