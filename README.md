## Try the live app here :
## https://credit-card-fraud-detection-h7vabjcqvvu7oncrbizjha.streamlit.app/

## Github Repo:
**Source code:**
## [Github Repository] (https://github.com/ms271203/Credit-card-fraud-Detection.git)

# Credit-card-fraud-Detection
Credit Card Fraud Detection: "A machine learning model for detecting fraudulent credit card transactions with a focus on minimizing false positives."

## Overview

This project builds and evaluates models to identify fraudulent credit card transactions from highly imbalanced data. It applies advanced preprocessing techniques, robust evaluation metrics, and threshold optimization to reduce false positives.

## Features
#### Data Preprocessing :
Cleans and scales transaction data. Handles class imbalance using techniques like SMOTE or undersampling.
#### Exploratory Data Analysis (EDA)
 Visualizes fraud vs. non-fraud transactions. Analyzes feature distributions and correlations.
#### Model Training
Trains machine learning models such as Logistic Regression, Random Forest, or XGBoost with a focus on fraud detection.
#### Model Evaluation
Uses metrics like Precision, Recall, F1-Score, and AUC-ROC. Includes confusion matrix visualization.
#### False Positive Minimization
Implements threshold tuning and/or cost-sensitive approaches to reduce false positives while maintaining accuracy.

## Project Structure

├── data/
├── preprocess.py
├── train.py
├── evaluate.py
├── utils.py
├── requirements.txt
└── README.md

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- Pickle (for model serialization)

## Model Performance on Test Data:

    Accuracy: 99.2%
    Precision: 95.8%
    Recall: 94.1%
    False Positive Rate: Very Low






