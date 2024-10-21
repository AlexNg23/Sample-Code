import streamlit as st

# Title for the app
st.title("Welcome to My Simple Streamlit App")

# Add a text input field
name = st.text_input("Enter your name:")

# Display a personalized greeting
if name:
    st.write(f"Hello, {name}! Welcome to the app.")

# Add a slider widget
age = st.slider("Select your age:", 18, 100)

# Display the selected age
st.write(f"You are {age} years old!")