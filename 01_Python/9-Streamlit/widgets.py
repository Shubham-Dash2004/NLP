import streamlit as st
import pandas as pd
st.title("Widgets in Streamlit")

name = st.text_input("Enter your name")

age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")



options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")




data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)