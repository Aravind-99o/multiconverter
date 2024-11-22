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
        options=["Select an option", "Centimeter to Meter", "Meter to Centimeter"],
        index=0, 
    )

        if convertion == "Select an option":
            st.write("Please select a valid convertion.")
        else:
            if convertion=="Centimeter to Meter":
                cm = st.slider("Select Length in Centimeter ", 0, 1000, 0)
                cmresult=cm/100
                st.title(f"{cmresult} M")
            if convertion=="Meter to Centimeter":
                mtr = st.slider("Select Length in Meter ",0.0, 10.0, 1.0, step=0.1)
                mtrresult=mtr*100
                st.title(f"{mtrresult} CM")


if unit=="Weight":
        convertion = st.selectbox(
        "Select convertion:",
        options=["Select an option", "mg to kg", "kg to Mg"],
        index=0, 
    )

        if convertion == "Select an option":
            st.write("Please select a valid convertion.")
        else:
            if convertion=="kg to mg":
                mg = st.slider("Select Weight in mg ", 0, 1000, 0)
                mgresult=mg/1000
                st.title(f"{mgresult} Kg")
            if convertion=="mg to kg":
                kg = st.slider("Select Weight in kg ",0.0, 10.0, 1.0, step=0.1)
                kgresult=kg*1000
                st.title(f"{kgresult} mg")
            
