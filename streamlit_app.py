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
                mtr = st.slider("Select Length in Meter ",0.0, 100.0, (25.0, 75.0))
                mtrresult=mtr*100
                st.title(f"{mtrresult} CM")
                
    
            
