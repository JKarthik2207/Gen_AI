import streamlit as st

st.title("Sum of the numbers in string")

a = st.text_input(label="Enter a String")
if st.button("Submit"):
    try:
        s=0
        for i in a:
            if i.isnumeric():
                s+=int(i)
        if(s==0):
            st.write("No number in string")
        else:
            st.write("The sum of numbers", s)
    except ValueError:
        st.write("Please enter a valid number (positive integer)")