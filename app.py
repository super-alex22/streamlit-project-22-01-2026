import streamlit as st
st.title("Login system")
name = st.text_input("Enter name")
if st.button("Check"):
  if name.strip()=="":
    st.warning("I'd like to kindly have you asked to enter text")
  elif not name.isalpha():
    st.warning("Warning")
  else:
    st.success("The text has been entered correctly")
