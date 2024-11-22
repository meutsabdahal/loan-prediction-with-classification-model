
# Loan Approval Prediction
This project predicts loan approval status using machine learning classification models. 


**Data:** https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data 

## Data Cleaning
    1. Capitalized the column values
    2. Outlier Removed (Age above 100 and income above 1 million)

## Feature Engineering
    1. Two new column added: income_to_loan ratio and net_disposable_income

## EDA
1. Loan Status According to Gender
![alt text](charts/loan_status_gender.png)

2. Loan Status According to Education Qualification
![alt text](charts/loan_status_education.png)

3. Loan Status According to Loan Intent
![alt text](charts/loan_status_intent.png)

4. Age Range
![alt text](charts/age_range.png)

5. Income Range
![alt text](charts/income_range.png)

6. Loan Range
![alt text](charts/loan_range.png)

7. Credit Range
![alt text](charts/credit_range.png)

8. Income vs Loan Amount
![alt text](charts/income_vs_loan.png)

9. HeatMap
![alt text](charts/heatmap.png)

## Data Processing
    1. Label Encoding is performed for categorical data
    2. Standarizaation is performed for numerical data

## Model Trainning
    1. Input Feature and Target Variable is assigned
    2. Train Test Split: 80% trainning and 20% testing
    3. Random Forest Classifier is used for trainning
        - Accuracy: 93.21% and Cross Validation: 92.54%
    4. Hyperparameter Tunning using GridSearchCV
        - Accuracy: 93.35% and Cross Validation: 92.67%
    5. Model Evaluation is performed classification Report and Confusion Matrix
![alt text](charts/confusion_matrix.png)
