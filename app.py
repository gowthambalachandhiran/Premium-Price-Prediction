import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Insurance Premium Calculator",
    page_icon="💰",
    layout="centered"
)

# Function to load model safely
def load_model(model_path='rf_regressor_selected_V1.pkl'):
    try:
        # Try loading with specific encoding
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.info("Please ensure the model was saved using sklearn 1.6.0 and joblib 1.4.2")
        return None

# Title and description
st.title("Insurance Premium Calculator")
st.write("Enter your health information to get a premium estimate")

# Create form
with st.form("insurance_form"):
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=30,
            help="Enter your age in years"
        )
        
        weight = st.number_input(
            "Weight (kg)",
            min_value=0,
            max_value=200,
            value=70,
            help="Enter your weight in kilograms"
        )
        
        height = st.number_input(
            "Height (cm)",
            min_value=0,
            max_value=250,
            value=170,
            help="Enter your height in centimeters"
        )
        
        num_surgeries = st.number_input(
            "Number of Major Surgeries",
            min_value=0,
            max_value=50,
            value=0,
            help="Enter the number of major surgeries you've had"
        )
    
    with col2:
        any_transplants = st.radio(
            "Any Transplants?",
            options=["No", "Yes"],
            index=0,
            help="Select if you've had any organ transplants"
        )
        
        chronic_diseases = st.radio(
            "Any Chronic Diseases?",
            options=["No", "Yes"],
            index=0,
            help="Select if you have any chronic diseases"
        )
        
        cancer_history = st.radio(
            "History of Cancer in Family?",
            options=["No", "Yes"],
            index=0,
            help="Select if there's a history of cancer in your family"
        )

    # Submit button
    submitted = st.form_submit_button("Calculate Premium")

# Process the form data when submitted
if submitted:
    # Convert radio button answers to binary
    any_transplants_binary = 1 if any_transplants == "Yes" else 0
    chronic_diseases_binary = 1 if chronic_diseases == "Yes" else 0
    cancer_history_binary = 1 if cancer_history == "Yes" else 0
    
    # Create input data frame
    input_data = pd.DataFrame({
        'Age': [age],
        'Weight': [weight],
        'AnyTransplants': [any_transplants_binary],
        'Height': [height],
        'NumberOfMajorSurgeries': [num_surgeries],
        'AnyChronicDiseases': [chronic_diseases_binary],
        'HistoryOfCancerInFamily': [cancer_history_binary]
    })
    
    try:
        # Load the model
        model = load_model()
        
        if model is not None:
            # Make prediction
            prediction = model.predict(input_data)[0]
            
            # Display result
            st.success(f"Estimated Premium: ${prediction:,.2f}")
            
            # Display risk factors if premium is high
            if prediction > 5000:
                st.warning("Factors that may be increasing your premium:")
                risk_factors = []
                if age > 60:
                    risk_factors.append("Age above 60")
                if any_transplants_binary:
                    risk_factors.append("History of transplants")
                if num_surgeries > 2:
                    risk_factors.append("Multiple major surgeries")
                if chronic_diseases_binary:
                    risk_factors.append("Presence of chronic diseases")
                if cancer_history_binary:
                    risk_factors.append("Family history of cancer")
                    
                for factor in risk_factors:
                    st.write(f"• {factor}")
                    
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        st.info("Please ensure your input data matches the expected format")

# Add some helpful information at the bottom
st.markdown("""
---
### About this Calculator
This tool uses a machine learning model to estimate insurance premiums based on various health factors. 
The estimate is for informational purposes only and may not reflect actual premium costs.

### Model Information
- Features used: Age, Weight, AnyTransplants, Height, NumberOfMajorSurgeries, AnyChronicDiseases, HistoryOfCancerInFamily
- Model type: Random Forest Regressor
- Required sklearn version: 1.6.0
- Required joblib version: 1.4.2
""")