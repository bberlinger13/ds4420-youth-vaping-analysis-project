# First Streamlit App!!

import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
IMAGE_DIR = BASE_DIR / "images"

st.set_page_config(page_title="MLP Results", layout="wide")

st.title("MLP Model Results")
st.subheader("Multilayer Perceptron Performance and Interpretation")

st.markdown("""
The manual multilayer perceptron (MLP) was used to capture complex, nonlinear
relationships between social media behavior and e-cigarette use that simpler
models might miss. Given the exploratory analysis, which showed multiple weak
predictors rather than one strong predictor, the MLP was a useful way to combine
these signals into a stronger overall prediction of at-risk adolescents.
""")

st.markdown("### Training Setup")
st.write("""
The model was trained on 80% of the combined dataset (about 10,070 observations)
and tested on the remaining 20% (about 2,518 observations). Training loss
decreased steadily over 600 epochs, dropping from about 0.79 to 0.63. Most of
the improvement happened early, especially in the first 50 epochs, and the loss
began to level off after around epoch 200.
""")

st.markdown("### Threshold Comparison")

results_df = pd.DataFrame({
    "Threshold": [0.5, 0.4, 0.3],
    "Accuracy": [0.633, None, 0.543],
    "Precision": [0.613, 0.552, 0.499],
    "Recall": [0.528, 0.709, 0.878],
    "F1 Score": [0.567, 0.621, 0.636]
})

st.dataframe(results_df, use_container_width=True)

st.markdown("### Key Interpretation")
st.write("""
At the default threshold of 0.5, the model had the highest accuracy (63.3%),
but it only identified 52.8% of actual e-cigarette users. Lowering the threshold
to 0.3 greatly improved recall to 87.8%, meaning the model identified most true
users, but this came with more false positives and lower overall accuracy.

Because this project is focused on a public health problem, missing at-risk
adolescents is more serious than incorrectly flagging some non-users. For that
reason, the 0.3 threshold was selected as the preferred operating point.
""")

st.markdown("### Final Takeaway")
st.success("""
Overall, the MLP performed moderately well. The results suggest that social media
and demographic variables capture meaningful patterns, but they do not fully
explain e-cigarette use on their own. The model is most useful as a screening
tool, especially at the 0.3 threshold where recall is highest.
""")

st.markdown("### Confusion Matrix Summary")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Threshold = 0.5")
    st.write("""
    - True Positives: 605  
    - False Positives: 382  
    - False Negatives: 541  
    - True Negatives: 990  
    """)

with col2:
    st.markdown("#### Threshold = 0.3")
    st.write("""
    - True Positives: 1006  
    - False Positives: 1010  
    - False Negatives: 140  
    - True Negatives: 362  
    """)

st.markdown("### Training Loss Curve")
st.image(str(IMAGE_DIR / "loss_curve.png"), caption="Training Loss Over Epochs")

st.markdown("### Confusion Matrix")
st.image(str(IMAGE_DIR / "confusion_matrix.png"), caption="MLP Confusion Matrices")