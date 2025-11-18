import streamlit as st
from model import train_model, predict
from recommender import generate_recommendations
import pandas as pd

st.title("HealthScope AI 💊")

menu = ["Predict Single Patient", "Batch Prediction (CSV)"]
choice = st.sidebar.selectbox("Choose Mode", menu)

if choice == "Predict Single Patient":
    st.subheader("Enter Patient Data")
    age = st.slider("Age", 10, 100, 30)
    bmi = st.slider("BMI (Body Mass Index)", 10.0, 50.0, 22.0)
    bp = st.slider("Blood Pressure (mm Hg)", 80, 200, 120)
    glucose = st.slider("Glucose Level (mg/dL)", 70, 200, 100)

    if st.button("Predict Risk"):
        models, scaler = train_model()
        input_features = [age, bmi, bp, glucose]
        results = predict(models, scaler, input_features)

        st.subheader("Disease Risk Prediction")
        for disease, prob in results.items():
            st.write(f"**{disease.capitalize()} Risk:** {prob*100:.2f}%")

        st.subheader("Personalized Health Tips")
        tips = generate_recommendations(age, bmi, bp, glucose)
        for tip in tips:
            st.markdown(f"- {tip}")

else:
    st.subheader("Upload CSV for Batch Prediction")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df)

        models, scaler = train_model()
        st.subheader("Predictions:")
        for i, row in df.iterrows():
            features = [row['age'], row['bmi'], row['blood_pressure'], row['glucose']]
            results = predict(models, scaler, features)
            st.write(f"Patient {i+1} Risk:")
            for disease, prob in results.items():
                st.write(f"- **{disease.capitalize()} Risk:** {prob*100:.2f}%")
            st.markdown("---")
            
# run : streamlit run app.py

# URL : https://healthscope-aigit-nsq68amrxyjyprqwxbwsaa.streamlit.app/