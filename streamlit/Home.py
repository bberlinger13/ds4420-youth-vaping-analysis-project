# First Streamlit App!!
import streamlit as st
import pandas as pd
import numpy as np
import time

# function to create a sample data frame and display it
def multi_pages():

    st.sidebar.markdown("## Home")
    st.write("# DS4420 Final Project")
    st.write('')
    st.write("Some info about vaping and why its bad blah balh ")

    st.write("## Here's a slider to do some math!")
    x = st.slider('x')  # 👈 this is a widget
    st.write('## ', x, 'squared is', x * x)

# Call the first_app() function
if __name__ == "__main__":
    multi_pages()