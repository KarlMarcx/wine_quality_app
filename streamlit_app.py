

import streamlit as st
import joblib
import pandas as pd

PIPELINE_PATH = "wine_quality_pipeline.joblib"
META_PATH = "metadata.joblib"

@st.cache_resource
def load_pipeline():
    pipeline = joblib.load(PIPELINE_PATH)
    meta = joblib.load(META_PATH)
    return pipeline, meta

pipeline, meta = load_pipeline()
feature_cols = meta['feature_cols']

st.title("Boutique Winery — Wine Quality Predictor")

with st.form("input_form"):
    st.subheader("Enter Wine Sample Features")
    input_data = {}
    cols = st.columns(2)
    for i, col in enumerate(feature_cols):
        with cols[i % 2]:
            val = st.number_input(col, value=0.0, format="%.6f")
            input_data[col] = val
    submitted = st.form_submit_button("Predict")

if submitted:
    sample = pd.DataFrame([input_data], columns=feature_cols)
    pred_prob = pipeline.predict_proba(sample)[0,1]
    pred_class = pipeline.predict(sample)[0]
    st.metric("Confidence (prob good)", f"{pred_prob:.3f}")
    if pred_class == 1:
        st.success(f"Prediction: GOOD (quality >= 7). Confidence: {pred_prob:.2%}")
    else:
        st.error(f"Prediction: NOT GOOD. Confidence: {1 - pred_prob:.2%}")
