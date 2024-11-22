import streamlit as st

st.title('Multi Converter')

st.write('This multi-converter application allows users to easily convert between different units of length, currency, and weight.The modular design makes it easy to extendwith additional conversion functionalities as needed.')

unit = st.selectbox(
    "select the unit to convert",
    ("Length", "Weight", "Currency","Speed"),
)

st.write("You selected:", unit)

if unit=="Length":
    convertion = st.selectbox(
    "select Covertion",
    ("Length Centimeter to Meter","Length Meter to Centimeter"),
    )
    if covertion=="Length Centimeter to Meter":
        age = st.slider("How old are you?", 0, 1000, 100)
    
