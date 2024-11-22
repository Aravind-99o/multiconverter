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
            if convertion=="g to kg":
                g = st.number_input("Insert a Weight in g")
                gresult=g/1000
                st.title(f"{gresult} Kg")
            if convertion=="kg to g":
                kg = st.number_input("Insert a Weight in kg")
                kgresult=kg*1000
                st.title(f"{kgresult} g")


if unit=="Currency":
    cur1=st.selectbox(
    "Select Currency:",["Select an option","Kuwaiti Dinar (KWD)", "Euro (EUR)","United States Dollar (USD)","Indian Rupee (INR)"],
    index=0, 
    )
            
    cur2=st.selectbox(
    "Select Currency:",["Select an option","Kuwaiti Dinar (KWD)", "Euro (EUR)","United States Dollar (USD)","Indian Rupee (INR)"],
    index=0, 
    )
    
    if convertion == "Select an option":
            st.write("Please select a valid convertion.")
    
    rate=[999,274.55,274.55,84.42,1]
    ext=["NA","KWD","EUR","USD","INR"]

   
        
    amount=st.slider("Select Amount", 0.0, 100000.0, 1.0, step=0.1)

        # ind_cur1=currency.index(cur1)

        # value1=rate[ind_cur1]

        # ind_cur2=currency.index(cur2)
        # value2=rate[ind_cur2]

        # indian=amount*value1
        # converted=indian/value2

        # extention=ext[ind_cur2]
        # st.title(f"{converted,extention}")
        
        
    



            
