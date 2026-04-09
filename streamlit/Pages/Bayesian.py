import streamlit as st
import pandas as pd
import numpy as np
import time
from pathlib import Path
import plotly.graph_objects as go
from pathlib import Path

# function to create a sample data frame and display it
def page01():

    @st.cache_data
    def load_data():
        base = Path(__file__).parent.parent.parent / "python" / "model_output"
        fixed_effects = pd.read_csv(base / "fixed_effects.csv")
        predicted_probs = pd.read_csv(base / "predicted_probs.csv")
        return fixed_effects, predicted_probs

    fixed_effects, predicted_probs = load_data()

    st.title("Youth E-Cigarette Use - Model Results")

    st.subheader("Model Coefficients")
    st.dataframe(fixed_effects)

    st.subheader("Predicted Probabilities by Platform")
    st.dataframe(predicted_probs)

    # --- Coefficient Plot ---
    st.subheader("Model Coefficients")

    # Remove intercept for cleaner plot
    plot_df = fixed_effects[fixed_effects["predictor"] != "Intercept"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=plot_df["Estimate"],
        y=plot_df["predictor"],
        mode="markers",
        marker=dict(size=8, color="steelblue"),
        error_x=dict(
            type="data",
            symmetric=False,
            array=plot_df["Q97.5"] - plot_df["Estimate"],
            arrayminus=plot_df["Estimate"] - plot_df["Q2.5"]
        ),
        name="Estimate"
    ))

    # Add vertical line at 0
    fig.add_vline(x=0, line_dash="dash", line_color="gray")

    fig.update_layout(
        xaxis_title="Log Odds",
        yaxis_title="Predictor",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)



# Call the first_app() function
page01()