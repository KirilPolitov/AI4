import streamlit as st

st.title("login")
name = st.text_input("enter name")
if st.button("check"):
 if name.strip() == " ":
  st.warning("please enter text")
 elif not name is alpha():
  st.warning("pls text")
 else st.success("good")
