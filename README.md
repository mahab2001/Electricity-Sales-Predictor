# 🔌 Electricity Sales Prediction

This is a machine learning-powered web app that predicts electricity sales based on historical data, pricing, customer count, and sectoral/region-specific features.

Built with **Streamlit**, the app provides an interactive UI for entering input features and viewing predicted sales instantly.

## 📊 Project Overview

The prediction model was trained on publicly available U.S. electricity sales data from the [EIA (U.S. Energy Information Administration)](https://www.eia.gov/), covering the period from **April 2024 to May 2025**.

Key features used in the model:
- Number of customers
- Electricity price
- Month
- Sector (Residential, Industrial, Commercial, Transportation)
- Region (e.g., South Atlantic, West South Central)

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy, scikit-learn**
- **Random Forest Regressor**
- **Streamlit** for deployment
- **Joblib** for model serialization

## 🔮 Model Performance

- **MAE**: 528.64
- **RMSE**: 2289.27
- **R²**: 0.9917  
> This indicates very strong predictive performance.




