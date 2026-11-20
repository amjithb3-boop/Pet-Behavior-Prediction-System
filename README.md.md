# Pet Behavior Prediction System

## Project Overview

The Pet Behavior Prediction System is a Machine Learning project that
predicts whether a pet is showing normal behavior or a possible
behavioral concern based on different behavioral indicators.

The system uses a trained Logistic Regression model and a Streamlit web
application to make predictions based on user inputs.

## Dataset Information

The dataset contains **4,997 records and 8 columns** after removing
duplicate rows.

### Input Features

-   Barking Frequency
-   Aggression Level
-   Anxiety Level
-   Activity Level
-   Social Interaction
-   Eating Habits
-   Sleep Disruptions

### Target Variable

`prediction`

-   `0` -- Normal Behavior
-   `1` -- Possible Behavioral Concern

## Machine Learning Workflow

The following steps were performed during the project:

1.  Data Loading
2.  Data Cleaning
3.  Exploratory Data Analysis (EDA)
4.  Handling Duplicate Records
5.  Feature and Target Separation
6.  Train-Test Split
7.  Feature Scaling using StandardScaler
8.  Model Training
9.  Model Evaluation
10. Cross-Validation
11. Hyperparameter Tuning using GridSearchCV
12. Error Analysis
13. Model Saving using Joblib
14. Streamlit Web Application Development

## Models Used

Three Machine Learning algorithms were trained and evaluated:

-   Logistic Regression
-   Decision Tree Classifier
-   Random Forest Classifier

## Model Comparison

  Model                   Accuracy   ROC-AUC
  --------------------- ---------- ---------
  Logistic Regression        97.2%     1.000
  Decision Tree              94.7%     0.965
  Random Forest              95.0%     0.989

## Final Model

Logistic Regression was selected as the final model based on its
cross-validation performance and evaluation results.

Hyperparameter tuning was performed using GridSearchCV.

-   **Best parameter:** `C = 100`
-   **Best cross-validation F1-score:** 96.64%
-   **Test accuracy after tuning:** 99.4%

## Installation and Usage

### Requirements

-   Python
-   NumPy
-   Scikit-learn
-   Streamlit
-   Joblib

### Install Required Libraries

Open Command Prompt in the project folder and run:

``` bash
pip install streamlit numpy scikit-learn joblib
```

### Run the Application

Make sure the following files are in the same project folder:

-   `app.py`
-   `pet_behavior_model.pkl`
-   `pet_behavior_scaler.pkl`

Run the Streamlit application:

``` bash
streamlit run app.py
```

The application will open in your web browser.

Enter the pet behavior details and click the **Predict Pet Behavior**
button to get a prediction.

## Limitations

-   This project is developed for educational purposes.
-   Predictions are based on the patterns in the available dataset.
-   The model is not a veterinary diagnostic tool.
-   Real-world pet behavior may depend on additional factors not
    included in the dataset.

## Future Improvements

-   Use a larger and more diverse dataset.
-   Explore additional machine learning algorithms.
-   Improve the user interface.
-   Test the model using real-world data.
