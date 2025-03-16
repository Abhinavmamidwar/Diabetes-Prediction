# Diabetes-Prediction

## Overview
This project is a **Streamlit-based web application** that predicts diabetes risk based on user-inputted health parameters. It utilizes a trained machine learning model (`final_model.pkl`) to provide real-time predictions.

## Features
- **Streamlit Web App** with interactive UI
- **Diabetes Risk Prediction** using a trained model
- **Data Insights** with visualizations
- **Information about Diabetes** for user awareness
- **Navigation System** for seamless user experience

## Dataset
The model is trained using a dataset containing health-related features:
- **Age**
- **Hypertension (0 = No, 1 = Yes)**
- **Heart Disease (0 = No, 1 = Yes)**
- **BMI (Body Mass Index)**
- **HbA1c Level**
- **Blood Glucose Level**

## Technologies Used
- **Python**
- **Streamlit** (Frontend)
- **Scikit-learn** (Model Training)
- **Pandas & NumPy** (Data Processing)
- **Matplotlib & Seaborn** (Data Visualization)
- **Pickle** (Model Storage)


## Usage
1. **Ensure the trained model (`final_model.pkl`) is in the project directory.**
2. **Run the Streamlit web app:**
   ```bash
   streamlit run app2.py
   ```
3. **Navigate through the app:**
   - 🏠 **Home** – Introduction to the app
   - 🔬 **Diabetes Prediction** – Input health details to predict diabetes risk
   - ℹ️ **About Diabetes** – Information about diabetes types and symptoms
   - 📊 **Data Insights** – Visual analytics on diabetes trends
   - 📞 **Contact** – Contact details for inquiries

## Model Details
- **Trained Model:** `final_model.pkl`
- **Feature Scaling:** Standardization (mean, standard deviation normalization)
- **Prediction Output:**
  - ✅ **Not Diabetic** – Maintain a healthy lifestyle
  - ⚠️ **Diabetic** – Consultation recommended, along with prevention tips


