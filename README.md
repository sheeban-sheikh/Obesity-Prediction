# Obesity Prediction Web App using Machine Learning

This project predicts whether a person is **Obese** or **Not Obese** based on user input using a trained **Logistic Regression Model**. The app is built using **Streamlit**, and the entire pipeline includes data cleaning, model training, saving model files, and a frontend interface.

---

## Live Demo

[Click Here to Try the Live App](https://sheeban-sheikh.streamlit.app/)

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Pickle
- Streamlit
- Jupyter Notebook

---

## Project Structure

```
obesity-prediction-app/
│
├── data/
│   ├── obesity_raw.csv
│   └── obesity_cleaned.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── ml.ipynb
│
├── model/
│   ├── model.pkl
│   └── scaler.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Model Performance (on test data)

- Accuracy: **96.67%**
- Precision: **96%**
- Recall: **92%**
- F1-score: **94%**

Confusion Matrix:
- True Positives (TP): Correctly predicted obese
- True Negatives (TN): Correctly predicted not obese
- False Positives (FP): Predicted obese but actually not
- False Negatives (FN): Predicted not obese but actually obese

---

## How to Run the App Locally

1. Clone the repository

```
git clone https://github.com/sheeban-sheikh/obesity-prediction-.git
cd obesity-prediction-
```

2. Create a virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate     (for Windows)
source venv/bin/activate  (for Mac/Linux)
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the app

```
streamlit run app.py
```

---

## Input Features

The app takes the following inputs from the user:

- Age
- Height
- Weight


These features are standardized using StandardScaler before prediction.

---

## Model Training Workflow

1. `data_cleaning.ipynb`:  
   - Loaded raw data  
   - Handled missing values and categorical encoding  
   - Exported cleaned dataset  

2. `ml.ipynb`:  
   - Loaded cleaned data  
   - Performed feature scaling  
   - Split data into train/test  
   - Trained Logistic Regression model  
   - Evaluated performance using accuracy, precision, recall, F1-score  
   - Saved trained model and scaler using Pickle

3. `app.py`:  
   - Built a web interface using Streamlit  
   - Took user inputs  
   - Scaled inputs using saved scaler  
   - Loaded model to make prediction  
   - Displayed result in real time

---

## requirements.txt

```
streamlit
pandas
numpy
scikit-learn
```

## Author

**Sheeban Sheikh**  
GitHub: [https://github.com/sheeban-sheikh](https://github.com/sheeban-sheikh)  
Email: work.sheeban@gmail.com

---

## License

This project is licensed under the MIT License.
