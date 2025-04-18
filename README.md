# Project title: Diabetes Web App

## Link to Diabetes Web App:[https://diabeteswebapp-xhk39r6xtrzauucr2nvcav.streamlit.app/](#https://diabeteswebapp-xhk39r6xtrzauucr2nvcav.streamlit.app/)

## Table of Contents
- [Acknowledgments](#acknowledgments)
- [Project Preview](#docs/project-preview.md)
- [Project Objective](#project-objective)
- [Project Significance](#project-significance)
- [Methodology](#methodology)
- [Prerequisites](#Prerequisities)
- [Discussion of Result](#discussion-of-result)
- [Conclusion](#conclusion)

## Project Preview
This project contains a web-based Diabetes Prediction System utilizing machine learning algorithms and Streamlit. The system predicts whether a patient has diabetes based on their medical characteristics.

## Project Objective
The main objective of this project is to develop a machine learning-based web application that predicts diabetes based on medical parameters. The application provides a user-friendly interface where users can input their medical details and receive an instant prediction of their diabetes status.

## Project Significance
- Provides quick and reliable diabetes prediction.
- Enhances accessibility for users without technical expertise.
- Uses machine learning to improve prediction accuracy.
- Aids in early detection and intervention for diabetes management.

## Features Used for Prediction
- The following medical features are used for prediction:
- Gender – The biological sex of the patient (Male or Female).
- AGE – The age of the patient in years.
- Urea – Urea level in the blood, an indicator of kidney function.
- Cr (Creatinine) – Creatinine level in the blood, used to assess kidney function.
- HbA1c (Glycated Hemoglobin) – Average blood sugar level over the past 2–3 months, a key diabetes indicator.
- Chol (Cholesterol) – Total cholesterol level in the blood, used to assess cardiovascular risk.
- TG (Triglycerides) – Type of fat (lipid) found in the blood, linked to heart disease and diabetes risk.
- HDL (High-Density Lipoprotein) – "Good" cholesterol, helps remove excess cholesterol from the bloodstream.
- LDL (Low-Density Lipoprotein) – "Bad" cholesterol, high levels increase the risk of heart disease.
- VLDL (Very Low-Density Lipoprotein) – Another form of bad cholesterol, contributes to plaque buildup in arteries.
- BMI (Body Mass Index) – A measure of body fat based on weight and height.
- CLASS – The target variable, representing the diabetes prediction outcome (e.g., No Diabetes, Diabetic, Predicted Diabetic, Mixed Prediction).

## Project Methodology
- Data Collection – Medical dataset containing patient records.
- Data Preprocessing – Cleaning, normalization, and feature selection.
- Model Training – Machine learning models trained on labeled data.
- Model Evaluation – Performance assessed using precision, recall, F1-score, and confusion matrix.
- Web Application Deployment – Model integrated into a Streamlit web app for easy accessibility.
- Model Performance

#### The performance of the diabetes prediction model was evaluated using a classification report and confusion matrix.

'' Classification Report

              precision    recall  f1-score   support

       0       0.99      1.00      0.99       250
       1       1.00      1.00      1.00       239
       2       1.00      1.00      1.00       256
       3       1.00      0.98      0.99       257
       4       0.99      1.00      0.99       258

accuracy                           1.00      1260
macro avg      1.00      1.00      1.00      1260
weighted avg   1.00      1.00      1.00      1260

Confusion Matrix

[[250   0   0   0   0]
 [  0 239   0   0   0]
 [  0   0 256   0   0]
 [  3   0   0 251   3]
 [  0   0   0   0 258]]''

The model achieved high accuracy, demonstrating strong predictive capability.

## Prerequisites
- To run this project locally, you need:
- Python 3.13.0
- Streamlit 1.42.2
- Joblib 1.4.2
- Numpy 2.2.3
- Scikit-learn 1.6.1

## Discussion of Results
- The model shows exceptional performance with an accuracy of 100% on the test set. The classification report and confusion matrix confirm that the model effectively distinguishes between diabetic and non-diabetic cases.

- This system is an important step towards leveraging AI in healthcare for early diabetes detection, which can lead to timely medical interventions and better health outcomes for individuals.

## Acknowledgments

Special thanks to my tutor, Mr. God'spower Amaha, Mr. Oke and the open-source community for providing resources that enabled the development of this project. Also, appreciation to all contributors who provided feedback for refining the system.

