# Premium Price Prediction
This is an assingment which will help claim adjudicators to evaluate premium price based on risk factors of claim holder

## **Overview**
This repository contains an assignment designed to assist claim adjudicators in evaluating premium prices based on the risk factors associated with claim holders. The project integrates exploratory data analysis (EDA), predictive modeling, and a Streamlit-based web application for an end-to-end solution.

## **Repository Structure**
- **`Model_for_predicing_Premium_Price.ipynb`**  
  A Jupyter Notebook dedicated to exploratory data analysis (EDA). It investigates how premium prices are influenced by demographic and customer risk factors.

- **`Insurance_Cost_Prediction_EDA.ipynb`**  
  This notebook focuses on building predictive models for premium price prediction. It includes:
  - Data preprocessing
  - Model development
  - Hyperparameter tuning
  - Model evaluation and interpretation

- **`app.py`**  
  A Streamlit web application that takes user inputs (e.g., demographic details, risk factors) and predicts the premium price in real-time.

- **Tableau Dashboard**  
  A set of dashboards showcasing:
  - Basic EDA results
  - Descriptive statistics
  - Visualization of factors influencing premium prices  
  **[[Tableau Link](https://public.tableau.com/app/profile/gowtham.balachandhiran/viz/PremiumPriceInsurance/PremiumPriceDescriptives)]

    ![image](https://github.com/user-attachments/assets/974c5ef4-8514-49f5-bc54-f78e0d86e1b5)


---

## **How to Use**

### **1. Prerequisites**
- Python 3.x installed on your system.
- Required libraries in `requirements.txt` installed (use `pip install -r requirements.txt`).
- Streamlit installed (`pip install streamlit`).

### **2. Running the Notebooks**
1. Open `Model_for_predicing_Premium_Price.ipynb` for EDA.
2. Run `Insurance_Cost_Prediction_EDA.ipynb` to explore model-building steps.

### **3. Launching the Web Application**
1. Navigate to the project directory in your terminal.
2. Run the following command to start the app:
   ```bash
   streamlit run app.py

### Features
1. Exploratory Data Analysis (EDA):

  Insights into demographic and risk factors affecting premium pricing.
  Visualizations to understand correlations and trends.

2. Predictive Modeling:

  Implements multiple machine learning models for premium price prediction.
  Optimized using hyperparameter tuning.
  
3. Interactive Web Application:

  User-friendly interface to input claim holder details.
  Predicts premium prices instantly using trained models.

4. Visual Dashboards:

Comprehensive Tableau dashboards for data insights.
Factors influencing premium prices and their visual representations.


## Future Enhancements
Integration of additional risk factors for enhanced prediction accuracy.
Support for more advanced ML models (e.g., deep learning).
Real-time data updates for dynamic predictions.
Enhanced visualizations with geographical and temporal trends.


## Contact
For questions or feedback, feel free to reach out via the repository’s issue tracker.

## Tags
#DataScience #MachineLearning #InsuranceTech #PremiumPrediction #EDA #Streamlit #Tableau
