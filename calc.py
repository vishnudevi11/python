import streamlit as st

st.title("🧮Calculator")

num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
operator=st.selectbox("Select operator",["+","-","*","/"]) #dropdown

if st.button("Calculate"):
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        result=num1/num2
    st.success(result)