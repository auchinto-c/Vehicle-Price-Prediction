# Vehicle-Price-Prediction

## Introduction
<hr>
This project aims to predict the selling price of cars depending on various features available. This project highlights the pipeline starting from data preprocessing, model development, prediction and finally a web ready deployment.
<br><br>

## Credits
<hr>

| **Tutorial** | [Krish Naik - Car Price Prediction](https://www.youtube.com/watch?v=p_tpQSY1aTs)                                   |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| **Code**     | [Krich Naik - Car-Price-Prediction](https://github.com/krishnaik06/Car-Price-Prediction)                           |
| **Dataset**  | [Kaggle - Vehicle Dataset from CarDekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) |
<br><br>

## Brief
<hr>

|           | **Version** | **Details**                                  |
|-----------|-------------|----------------------------------------------|
| **Demo**  | v1          | [Heroku](https://car-price-v1.herokuapp.com) |
| **Model** | v1          | Random Forest Regression                     |

## Procedure
<hr>

1. Read the data from CSV into dataframes.
2. Understanding the data
   1. **Target Variable**: Selling_Price
   2. **Features**:
      1. **Categorical Features**:
         1. Fuel_Type - ['Petrol', 'Diesel', 'CNG']
         2. Seller_Type - ['Dealer', 'Individual']
         3. Transmission - ['Manual', 'Automatic']
         4. Owner - [0, 1, 3]
      2. **Quantitative Features**:
         1. Year
         2. Present_Price
         3. Kms_Driven
3. Data Preprocessing
   1. Check for Missing or Null values
   2. Derive Features from existing columns
      1. Get the Number of years, from the Year column, assuming current year is 2022.
      2. Represent the cateogrical variables, in integers, while flattening the columns with respect to each category value. Avoid Dummy Variable Trap.
4. Check for Correlation of features and target variables. This can help in feature selection in the future. The features can also be analysed with respect to their calculated feature importance.
5. Split the dataset into, train and test groups.
6. Initialize the set of options for various hyper=parameters for the specific model. Use the optimal combination of hyper-paramter values.
7. Initialize the Regressor Model.
8. Train the model on the training data set.
9. Make predictions on the test data set, using the trained model.
10. The predictions can be compared to actual recorded data of the test set.
11. Save the model as pickle file, this is a serialized file, that is used in deploying the model.
12. Implement app.py and index.html, to build a platform that can be used to show case the actual functioning model.
13. Deploy the project to heroku.
<br><br>

## Local Setup
<hr>

1. Clone the repository to your local system.
2. Run the `vehicle-price-prediction.ipynb` file on Jupyter notebook, to get the script of the model development and training.
3. To run the web portal using the model, run the `app.py` file. Modify `templates` folder to elaborate on the web front end.
<br><br>

## Library and Tools
<hr>

### Language
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML 5](https://img.shields.io/badge/html-%23323330.svg?style=for-the-badge&logo=html5&logoColor=%23F7DF1E)

### Data Analysis
![pandas](https://img.shields.io/badge/pandas-%23281f4f.svg?style=for-the-badge&logoColor=white)
![numpy](https://img.shields.io/badge/numpy-%23548ecc.svg?style=for-the-badge&logoColor=white)

### Model Development
![scikit-learn](https://img.shields.io/badge/scikit-learn-%23cc8854.svg?style=for-the-badge&logoColor=white)

### Visualizations
![matplotlib](https://img.shields.io/badge/matplotlib-%230e4e5e.svg?style=for-the-badge&logoColor=white)
![seaborn](https://img.shields.io/badge/seaborn-%23358f4b.svg?style=for-the-badge&logoColor=white)

### Model Serialisation
![pickle](https://img.shields.io/badge/pickle-%23634f0c.svg?style=for-the-badge&logoColor=white)

### Web Framework
![Flask](https://img.shields.io/badge/Flask-%23154718.svg?style=for-the-badge&logo=flask&logoColor=white)

### Deployment
![Heroku](https://img.shields.io/badge/heroku-%23a65dba.svg?style=for-the-badge&logo=heroku&logoColor=white)
<br><br>

## Results
<hr>

The trained model predictions over the test data set, was scatter plotted against the corresponding actual values from the test data set. We can observe that the points are almost following the `y=1` line. This means that the predictions are made close to the actual values.

![img](https://github.com/auchinto-c/Vehicle-Price-Prediction/blob/main/Visualizations/visualize_predicted_scatter.png)

<br>

The difference between the predictions and the actual values from the test set, was plotted as a distribution. This can be considered as the error distribution between predictions and actual values. We can observe that the spread is minute for this distribution, i.e. the predictions were made close to actual values.

![img](https://github.com/auchinto-c/Vehicle-Price-Prediction/blob/main/Visualizations/visualize_predicted_dist.png)
<br><br>

## Future Scope
<hr>

1. In future versions, we can explore the effects of feature selection, based on correlations and feature importance, on the model's accuracy.
2. In `version-1` we have used `Random Forest` as the Regression model. In future, we can explore different kinds of regression models, starting with simpler linear regression to other ensemble techniques.
3. Visualize the accuracies from different models. Develop a pipeline to explore multiple models, and select the model with highest accuracy.
4. Improve the UI of the web portal. Better design and readability.