import streamlit as st

st.title("login")
name = st.text_input("enter name")
age = st.number_input("enter age")
if st.button("check") and age >= 18:
 if name.strip() == "":
  st.warning("please enter text")
 elif not name.isalpha():
  st.warning("pls text")
 else: st.success("good")
else: st.warning("wait a few years")
