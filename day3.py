import streamlit as st

st.header("st.button")

if st.button("Say Hello", help="hey!"):
    st.write("Goodbye")
else:
    st.write("Why Hello there")