import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app")


name=st.text_input("What's your name?")
if name:
    st.success(f"Hello,{name}!")