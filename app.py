import streamlit as st
import joblib

st.title("🛍️ Customer Segmentation")

st.write("🚀 App started")

try:
    model = joblib.load("model.pkl")
    st.write("✅ Model loaded")
except Exception as e:
    st.error(f"❌ Model error: {e}")

income = st.number_input("Annual Income", 0)
purchase = st.number_input("Purchase Amount", 0)

if st.button("Predict Segment"):
    try:
        cluster = model.predict([[income, purchase]])[0]
        st.success(f"Customer belongs to Cluster: {cluster}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
