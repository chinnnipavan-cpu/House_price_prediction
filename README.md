# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project predicts house sale prices using the **Linear Regression** algorithm from Scikit-learn. It is built using the **House Prices - Advanced Regression Techniques** dataset from Kaggle.

The project demonstrates the complete Machine Learning workflow, from data preprocessing to model evaluation and saving the trained model.

---

## 🎯 Objective

The objective of this project is to build a machine learning model that can predict the selling price of a house based on various features such as area, number of rooms, year built, neighborhood, and more.

---

## 📂 Dataset

- **Dataset:** House Prices - Advanced Regression Techniques
- **Source:** Kaggle
- **Rows:** 1460
- **Columns:** 81

Target Variable:
- **SalePrice**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📊 Machine Learning Workflow

- Load Dataset
- Data Exploration
- Data Cleaning
- Handle Missing Values
- Feature Engineering
- Encode Categorical Variables
- Train-Test Split
- Train Linear Regression Model
- Predict House Prices
- Evaluate Model
- Save Trained Model

---

## 📈 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Performance

| Metric | Value |
|--------|-------:|
| MAE | 20436.78 |
| MSE | 2736914087.72 |
| RMSE | 52315.52 |
| R² Score | 0.643 |

---

## 📊 Visualizations

The project includes:

- Missing Value Analysis
- Feature Correlation Heatmap
- Actual vs Predicted House Prices
- Distribution of House Prices

---

## 📁 Project Structure

```
House-Price-Prediction/
│
├── train.csv
├── cleaned_house_data.csv
├── notebook.ipynb
├── house_price_model.pkl
├── README.md
```

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone https://github.com/chinnnipavan-cpu/House_price_prediction.git
```

2. Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

3. Open the Jupyter Notebook.

```bash
jupyter notebook
```

4. Run all cells.

---

## 📚 Concepts Covered

- Supervised Learning
- Linear Regression
- Feature Engineering
- Data Preprocessing
- One-Hot Encoding
- Train-Test Split
- Model Evaluation
- Model Serialization using Joblib

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Feature Selection
- Random Forest Regressor
- XGBoost Regressor
- Gradient Boosting
- Streamlit Web Application Deployment

---

## 👨‍💻 Author

**R. Pavan Kumar**

B.Tech CSE (AI & ML)

Machine Learning Enthusiast

---

## ⭐ Acknowledgements

- Kaggle for providing the dataset.
- Scikit-learn for the Linear Regression implementation.
- Andrew Ng's Machine Learning course for the theoretical concepts behind Linear Regression.