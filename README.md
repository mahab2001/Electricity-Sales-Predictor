# 🔌 Electricity Sales Prediction

This is a machine learning-powered web app that predicts electricity sales based on historical data, pricing, customer count, and sectoral/region-specific features.

Built with **Streamlit**, the app provides an interactive UI for entering input features and viewing predicted sales instantly.

## 📊 Project Overview

⚙️ Project Overview
Electricity Sales Predictor is an end-to-end machine learning project that estimates electricity sales across sectors and regions in the U.S. The app allows users to input specific features—such as the number of customers, price per unit, month, sector, and region—and predicts expected electricity sales.

This project follows the full data pipeline from data acquisition to deployment, demonstrating practical data science workflows.

🔄 Data Pipeline Workflow
1. 📡 Data Collection
The dataset was sourced from the U.S. Energy Information Administration (EIA), a real and credible open data provider.

Data includes monthly electricity sales across multiple states and sectors (residential, commercial, industrial, transportation).

Initial raw datasets were accessed manually and through API documentation provided by EIA.


2. 🧹 Data Preprocessing
Loaded and cleaned using pandas in Google Colab.

Tasks included:

Handling missing values.

Formatting dates and converting data types.

Encoding categorical features (e.g., sector and region IDs).

Feature engineering (e.g., extracting month).


3. 📊 Exploratory Data Analysis
Visualizations generated with Matplotlib and Seaborn to uncover:

Top-performing regions and sectors by sales.

Temporal sales patterns.

Summary statistics were computed to support insights.


4. 🧠 Model Building
Trained a Random Forest Regressor using the cleaned dataset.

Feature importance was analyzed—key features included:

customers, price, sector, region, and month.

5. ✅ Model Evaluation
Model achieved high performance:

R²: 0.9917

MAE: 528.64

RMSE: 2289.27

Performance metrics were computed using Scikit-learn.


6. 📦 Model Serialization
Final model exported using joblib and saved as model.joblib.


7. 🌐 Web App Deployment
Interactive app built using Streamlit.

Deployed to Streamlit Community Cloud.

App allows users to input new values and get real-time sales predictions.

📂 Tech Stack
Python: Core language

Pandas / NumPy: Data manipulation

Matplotlib / Seaborn: Data visualization

Scikit-learn: Model building and evaluation

Joblib: Model serialization

Streamlit: Frontend and deployment

Google Colab + GitHub: Development + version control

