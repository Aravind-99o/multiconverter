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
                cm =  st.number_input("Insert a Length in cm")
                cmresult=cm/100
                st.title(f"{cmresult} M")
            if convertion=="Meter to Centimeter":
                mtr = st.number_input("Insert a Length in meter")
                mtrresult=mtr*100
                st.title(f"{mtrresult} CM")


if unit=="Weight":
        convertion = st.selectbox(
        "Select convertion:",
        options=["Select an option", "g to kg", "kg to g"],
        index=0, 
    )

        if convertion == "Select an option":
            st.write("Please select a valid convertion.")
        else:
            if convertion=="kg to g":
                g = st.number_input("Insert a Weight in g")
                gresult=g/1000
                st.title(f"{gresult} Kg")
            if convertion=="g to kg":
                kg = st.number_input("Insert a Weight in kg")
                kgresult=kg*1000
                st.title(f"{kgresult} g")



            
