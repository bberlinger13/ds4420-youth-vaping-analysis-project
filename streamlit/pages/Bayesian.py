import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path


@st.cache_data
def load_data():
    base = Path(__file__).parent.parent.parent / "python" / "model_output"
    fixed_effects = pd.read_csv(base / "fixed_effects.csv")
    predicted_probs = pd.read_csv(base / "predicted_probs.csv")
    return fixed_effects, predicted_probs


fixed_effects, predicted_probs = load_data()


def page01():

    st.title("Bayesian Logistic Regression: E-Cigarette Use & Social Media")

    st.markdown("""
    This model estimates the association between social media exposure to e-cigarette 
    content and current e-cigarette use among U.S. youth, using data from the 
    National Youth Tobacco Survey 2021–2023 .

    A Bayesian logistic regression was fit using the brms package in R. 
    Predictors whose credible intervals exclude zero are considered credible predictors 
    of current use. The model achieved a Bayesian R² of 0.079.

    **Key findings:**
    - Frequency of seeing, posting, and interactingwith e-cigarette content 
      on social media were all positively associated with current use
    - More active engagement (posting, interacting) showed slightly stronger associations 
      than passive exposure (seeing content)
    - General social media use showed no credible association with e-cigarette use
    - Following public health creators was the strongest negative predictor,
    """)

    st.divider()

    # --- Coefficient Plot ---
    st.subheader("Model Coefficients")
    st.caption("Predictors to the right of zero are positively associated with e-cigarette use.")

    plot_df = fixed_effects[fixed_effects["predictor"] != "Intercept"].copy()
    plot_df = plot_df.sort_values("Estimate")

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

    fig.add_vline(x=0, line_dash="dash", line_color="gray")

    fig.update_layout(
        xaxis_title="Log-Odds Estimate (95% Credible Interval)",
        yaxis_title=None,
        height=600,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)




page01()