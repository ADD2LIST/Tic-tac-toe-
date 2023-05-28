import streamlit as st

def calculator():

    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")

    operator = st.selectbox("Select an operator:", ("+", "-", "*", "/"))

    num2 = st.number_input("Enter the second number:")

    result = 0

    if operator == "+":

        result = num1 + num2

    elif operator == "-":

        result = num1 - num2

    elif operator == "*":

        result = num1 * num2

    elif operator == "/":

        if num2 != 0:

            result = num1 / num2

        else:

            st.error("Error: Division by zero!")

    st.write("Result: ", result)

calculator()

