import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pickle


# Load Model
with open("final_model.pkl", 'rb') as file:
    loaded_model = pickle.load(file)

# Define valid pages
valid_pages = ["Home", "Diabetes Prediction", "About Diabetes", "Data Insights", "Contact"]

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Callback function for navigation
def change_page(selected_page):
    st.session_state["page"] = selected_page

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", valid_pages, index=valid_pages.index(st.session_state["page"]), on_change=change_page, args=(st.session_state["page"],))

# Home Page
if page == "Home":
    st.title("🏠 Welcome to the Diabetes Prediction App")
    st.write("This app helps predict the risk of diabetes based on user inputs.")

# Diabetes Prediction Page
elif page == "Diabetes Prediction":
    st.title("🔬 Diabetes Prediction")
    st.write("Enter your details below to check your diabetes risk.")
    
    # Display form to enter input values
    with st.form("prediction_form"):
        age = st.slider('Age', 0, 100, 50)
        hypertension = st.slider('Hypertension', 0, 1, 0)
        heart_disease = st.slider('Heart Disease', 0, 1, 0)
        bmi = st.slider('BMI', 10.0, 50.0, 25.0, step=0.1)
        HbA1c_level = st.slider('HbA1c Level', 4.0, 15.0, 7.0, step=0.1)
        blood_glucose_level = st.slider('Blood Glucose Level', 50, 400, 100)
        submitted = st.form_submit_button("🔍 Predict")
    
    # Function to scale features
    def scale_features(*values):
        mean_values = [41.88, 0.07, 0.039, 27.32, 5.52, 138.05]
        std_values = [22.51, 0.26, 0.19, 6.63, 1.07, 40.70]
        return [(x - mean) / std for x, mean, std in zip(values, mean_values, std_values)]

    # Perform prediction
    if submitted:
        prediction = loaded_model.predict([scale_features(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level)])

        if prediction[0] == 1:
            st.error("⚠️ **Diabetic** - Please consult a doctor.")
            
            # Show reasons for diabetes risk
            st.subheader("📌 Possible Reasons:") 
            reasons = []
            if age > 45:
                reasons.append("Age over 45 increases the risk of Type 2 Diabetes.")
            if hypertension == 1:
                reasons.append("High blood pressure is linked to insulin resistance.")
            if heart_disease == 1:
                reasons.append("Heart disease can be associated with metabolic disorders.")
            if bmi > 30:
                reasons.append("High BMI is a strong risk factor for diabetes.")
            if HbA1c_level > 6.5:
                reasons.append("Elevated HbA1c level indicates poor blood sugar control.")
            if blood_glucose_level > 200:
                reasons.append("High blood glucose level suggests uncontrolled diabetes.")

            for reason in reasons:
                st.write(f"✅ {reason}")

            # Tips for managing diabetes
            st.subheader("💡 How to Control Diabetes:")
            st.write("""
            - 🥗 **Eat Healthy:** Reduce sugar and refined carbs.
            - 🏃 **Exercise Regularly:** Aim for 30 minutes of activity per day.
            - 💧 **Stay Hydrated:** Drink enough water daily.
            - 🛌 **Manage Stress & Sleep:** Reduce stress and get quality sleep.
            - 💊 **Medication & Monitoring:** Follow doctor's advice and monitor sugar levels.
            """)
        else:
            st.success("✅ **Not Diabetic** - Keep maintaining a healthy lifestyle!")
            st.subheader("🛡️ Preventive Measures:")
            st.write("""
            - ✅ Maintain a **healthy weight**.
            - ✅ Eat a **balanced diet** rich in fiber and protein.
            - ✅ Exercise **regularly** (walking, jogging, gym).
            - ✅ Reduce **sugar and processed foods**.
            - ✅ Have **regular check-ups** with your doctor.
            """)

    # Add refresh button to refresh the result
    if st.button("🔄 Refresh Prediction"):
        st.rerun()

elif page == "About Diabetes":
    st.title("ℹ️ About Diabetes")
    st.write("""
    Diabetes is a chronic condition that affects how your body processes blood sugar.
    There are two main types:
    - **Type 1**: The body does not produce insulin.
    - **Type 2**: The body does not use insulin properly.
    
    **Common Symptoms:**  
    ✅ Frequent urination  
    ✅ Excessive thirst  
    ✅ Unexplained weight loss  
    ✅ Fatigue  
    """)

elif page == "Data Insights":
    st.title("📊 Data Insights")
    st.write("Here, we will show trends and analytics about diabetes cases.")
    age_groups = ["0-20", "21-40", "41-60", "61+"]
    diabetes_cases = [10, 35, 50, 70]
    fig, ax = plt.subplots()
    ax.bar(age_groups, diabetes_cases, color=["blue", "green", "orange", "red"])
    ax.set_xlabel("Age Groups")
    ax.set_ylabel("Diabetes Cases (%)")
    ax.set_title("Diabetes Cases by Age Group")
    st.pyplot(fig)

elif page == "Contact":
    st.title("📞 Contact Us")
    st.write("For any inquiries, please email us at: **support@diabetesapp.com**")
    st.text("📍 Address: Abhi HealthTech Solutions, 123 Abinav Medical Street, XYZ City, India")

# Navigation Buttons
col1, _, col2 = st.columns([1, 8, 1])
if col1.button("⬅️"):
    st.session_state["page"] = valid_pages[(valid_pages.index(page) - 1) % len(valid_pages)]
    st.rerun()
if col2.button("➡️"):
    st.session_state["page"] = valid_pages[(valid_pages.index(page) + 1) % len(valid_pages)]
    st.rerun()
