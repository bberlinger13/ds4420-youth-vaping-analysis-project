# First Streamlit App!!
import streamlit as st
import pandas as pd
import numpy as np
import time

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Youth Vaping Analysis",
    layout="wide"
)

def home_page():
    st.sidebar.markdown("## Navigation")
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        <div style='padding: 1.5rem 0;'>
            <h1 style='margin-bottom:0;'> Youth Vaping Analysis Dashboard</h1>
            <h4 style='margin-top:0; color:gray;'>DS4420 Final Project · Northeastern University</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        This dashboard examines how **social media exposure**, **demographic factors**, and
        **environmental influences** are associated with **youth e-cigarette use**.
        It compares an **MLP neural network** and **Bayesian logistic regression**
        to evaluate both predictive performance and interpretability.
        """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("Years of Data", "2021–2023")
    col2.metric("Primary Outcome", "Current Vaping")
    col3.metric("Modeling Approaches", "Bayesian + MLP")

    st.markdown("---")

    left, right = st.columns([1.7, 1])

    with left:
        st.markdown("### About the Project")
        st.write(
            """
            The purpose of this project is to better understand the factors associated
            with adolescent vaping behavior using NYTS survey data.
            The application includes:
            - exploratory data analysis
            - model results
            - comparisons across methods
            - interpretable findings for key predictors
            """
        )

    with right:
        st.markdown("### App Sections")
        st.write(
            """
            - **Home**: project summary  
            - **EDA**: trends and patterns  
            - **MLP**: predictive model results  
            - **Bayesian**: coefficient interpretation  
            """
        )

    st.markdown("---")

    st.markdown("### Dataset Preview")
    try:
        df = pd.read_csv("../data/cleaned/nyts_2021_2023_clean.csv")
        st.dataframe(df.head(), use_container_width=True)
    except FileNotFoundError:
        st.error("Could not find the cleaned dataset. Make sure the file path is correct.")

    st.markdown("---")
    st.caption("Created by Blythe Berlinger and Sydney Schulz")

if __name__ == "__main__":
    home_page()