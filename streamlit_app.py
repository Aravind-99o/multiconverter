import streamlit as st

st.title('Multi Converter')

st.write('This multi-converter application allows users to easily convert between different units of length, currency, and weight.The modular design makes it easy to extendwith additional conversion functionalities as needed.')

unit = st.selectbox(
    "select the unit to convert",
    ("Length", "Weight", "Currency","Speed"),
)

st.write("You selected:", unit)

if unit=="Length":
    location = st.selectbox(
    "Choose your location:",
    options=["Choose your location", "New York", "Los Angeles", "Chicago", "Houston"],
    index=0,  # Ensure the placeholder is the default selection
)

# Handle the user's selection
if location == "Choose your location":
    st.write("Please select a valid location.")
else:
    st.write(f"You selected: {location}")
   # conversion = st.selectbox(
   #  "Select Conversion",
   #  ("Select an option", "Length Centimeter to Meter", "Length Meter to Centimeter"),
   #  index=0  # Explicitly set the default index to the first item
   #  )
   #  if convertion=="Length Centimeter to Meter":
   #      cm = st.slider("Select Length in Centimeter ", 0, 1000, 100)
    
