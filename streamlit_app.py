import streamlit as st

st.title('Multi Converter')

st.write('This multi-converter application allows users to easily convert between different units of length, currency, and weight.The modular design makes it easy to extendwith additional conversion functionalities as needed.')

unit = st.selectbox(
    "Choose your location:",
    options=["Choose Unit to convert","Length","Weight","Currency"],
    index=0, 
)

if unit == "Choose Unit to convert":
    st.write("Please select a valid Unit.")
else:
    st.write(f"You selected: {unit}")

    if unit=="Length":
        convertion = st.selectbox(
        "Select convertion:",
        options=["Select an option", "Centimeter to Meter", "Meter to Centimetr"],
        index=0, 
    )

        if convertion == "Select an option":
            st.write("Please select a valid convertion.")
        else:
            st.write(f"You selected: {convertion}")
   # conversion = st.selectbox(
   #  "Select Conversion",
   #  ("Select an option", "Length Centimeter to Meter", "Length Meter to Centimeter"),
   #  index=0  # Explicitly set the default index to the first item
   #  )
   #  if convertion=="Length Centimeter to Meter":
   #      cm = st.slider("Select Length in Centimeter ", 0, 1000, 100)
    
