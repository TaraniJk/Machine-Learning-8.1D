# SIT720 Task 8.1D – Sydney Housing Price Prediction and Decision Support System

## Project Overview

This project was developed for SIT720 Machine Learning Task 8.1D. The aim of the project is to investigate residential property prices across three Sydney suburbs and develop a machine learning based decision-support system for estimating property sale prices.

The project covers the complete machine learning workflow, including data collection, data preparation, exploratory data analysis, feature engineering, model development, model evaluation, prediction error analysis, comparison of human, LLM and machine learning estimates, and deployment of the selected model through a Streamlit web application.

## Dataset

The dataset contains 100 manually collected sold residential properties from three Sydney suburbs:

- Parramatta – 34 properties
- Ryde – 35 properties
- Blacktown – 31 properties

The collected attributes include:

- Suburb
- Address
- Sale price
- Bedrooms
- Bathrooms
- Car spaces
- Property type
- Land size
- Floor area
- Sale date

The dataset is provided in `sydney_housing_data.xlsx`.

## Machine Learning Models

Three regression approaches were evaluated:

1. Linear Regression
2. Random Forest Regression
3. Gradient Boosting Regression

The models were evaluated using 5-fold cross-validation with:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Gradient Boosting achieved the strongest overall cross-validation performance and was selected for the final decision-support application.

## Human vs Machine Comparison

Ten properties were held out from the model-development process. Their actual sale prices were compared against:

- Human estimates
- LLM-generated estimates
- Gradient Boosting predictions

This comparison was used to examine the strengths and limitations of different property-price estimation approaches.

## Streamlit Application

A simple Streamlit web application was developed to demonstrate how the trained machine learning model can be used as a property-price decision-support tool.

The application accepts:

- Suburb
- Property type
- Number of bedrooms
- Number of bathrooms
- Number of car spaces

It then produces an estimated sale price using the trained Gradient Boosting regression model.

The application is intended for educational and decision-support purposes only and should not be treated as a professional property valuation.

## Repository Files

- `SIT720_8.1D.ipynb` – Complete machine learning analysis and model development
- `sydney_housing_data.xlsx` – Property dataset
- `app.py` – Streamlit web application
- `gradient_boosting_model.pkl` – Saved trained Gradient Boosting model
- `README.md` – Project documentation

## Running the Application

Install the required Python packages:

```bash
pip install pandas numpy scikit-learn streamlit