import streamlit as st

import math

def add(num1, num2):

    return num1 + num2

def subtract(num1, num2):

    return num1 - num2

def multiply(num1, num2):

    return num1 * num2

def divide(num1, num2):

    if num2 != 0:

        return num1 / num2

    else:

        st.error("Error: Division by zero!")

        return None

def square(num):

    return num ** 2

def square_root(num):

    if num >= 0:

        return math.sqrt(num)

    else:

        st.error("Error: Invalid input for square root!")

        return None

def calculator():

    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")

    operator = st.selectbox("Select an operator:", ("+", "-", "*", "/", "Square", "Square Root"))

    

    result = 0

    if operator == "+":

        num2 = st.number_input("Enter the second number:")

        result = add(num1, num2)

    elif operator == "-":

        num2 = st.number_input("Enter the second number:")

        result = subtract(num1, num2)

    elif operator == "*":

        num2 = st.number_input("Enter the second number:")

        result = multiply(num1, num2)

    elif operator == "/":

        num2 = st.number_input("Enter the second number:")

        result = divide(num1, num2)

    elif operator == "Square":

        result = square(num1)

    elif operator == "Square Root":

        result = square_root(num1)

    if result is not None:

        st.write("Result: ", result)

calculator()
