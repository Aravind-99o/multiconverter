import streamlit as st

st.title('Multi Converter')

st.write('This multi-converter application allows users to easily convert between different units of length, currency, and weight.The modular design makes it easy to extendwith additional conversion functionalities as needed.')

unit = st.selectbox(
    "select the unit to convert",
    ("Length", "Weight", "Currency","Speed"),
)

st.write("You selected:", unit)

if unit=="Length":
   conversion = st.selectbox(
    "Select Conversion",
    ("Select an option", "Length Centimeter to Meter", "Length Meter to Centimeter"),
    )

    if conversion == "Select an option":
    st.write("Please select a valid option.")
    else:
    st.write(f"You selected: {conversion}")
if convertion=="Length Centimeter to Meter":
    age = st.slider("Select Length in Centimeter ", 0, 1000, 100)
    
