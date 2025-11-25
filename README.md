# Heart Disease Prediction Streamlit App

A machine learning app built with Streamlit that predicts the risk of heart disease for a client based on health parameters like age, cholesterol, chest pain type, and more. The app uses a Random Forest classifier and provides risk probability.

## Features
- Predicts heart disease risk (High/Low) with probability
- User-friendly input interface using Streamlit
- Handles inputs like Age, Sex, Chest Pain Type, Resting BP, Cholesterol, Fasting Blood Sugar, ECG, Heart Rate, Exercise Angina, Oldpeak, ST Slope

## Installation

1. Clone the repo:
```bash
git clone https://github.com/ShreyaVaghasiya01/Heart-Disease-Prediction-Streamlit.git
```
2.Navigate to the project folder:
```bash
cd Heart-Disease-Prediction-Streamlit
```
3.Install required packages:
```bash
pip install -r requirements.txt
```
4.Run the Streamlit app:
```bash
streamlit run app.py
```
#Dataset

The app uses the Heart Statlog (Cleveland, Hungary, Switzerland, Long Beach VA) dataset. CSV file included in the repo: heart_statlog_cleveland_hungary_final.csv.

#Model

-Random Forest Classifier trained on the dataset

-Input features are scaled using StandardScaler (scaler_heart_disease.pkl)

-Model and scaler are saved as .pkl files

## User-Friendly Input Mapping

| Feature             | Options for Users                                  | Model Input       |
|--------------------|---------------------------------------------------|-----------------|
| Sex                | Male / Female                                     | 1 / 0           |
| Chest Pain Type    | Typical / Atypical / Non-anginal / Asymptomatic  | 0 / 1 / 2 / 3   |
| Fasting Blood Sugar| ≤120 mg/dl (Normal) / >120 mg/dl (High)         | 0 / 1           |
| Resting ECG        | Normal / ST-T abnormality / LVH                  | 0 / 1 / 2       |
| Exercise Angina    | No / Yes                                         | 0 / 1           |
| Oldpeak            | Numeric input (0.0–10.0)                        | Float           |
| ST Slope           | Upsloping / Flat / Downsloping                   | 1 / 2 / 3       |


#Technologies Used

-Python

-Streamlit

-Scikit-learn

-NumPy & Pandas

#Acknowledgements

-Heart Disease dataset from UCI Machine Learning Repository




