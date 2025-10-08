# 🩺 Diabetes Prediction Web App

This is a simple **Machine Learning Web Application** that predicts whether a person is diabetic or not based on medical input data.  
It uses a trained ML model and a **Streamlit** web interface for user interaction.

---

## 🚀 Project Overview

- **Model Type:** Supervised Machine Learning (Classification)
- **Framework:** Streamlit
- **Libraries Used:** Scikit-learn, Pandas, NumPy, Pickle
- **Language:** Python

The user provides health data such as glucose level, BMI, insulin level, etc., and the app predicts if the person is likely to have diabetes.

---

## 🧠 How It Works

1. The ML model (trained using the Pima Indians Diabetes Dataset) is loaded with `pickle`.
2. The user inputs health parameters through a Streamlit web form.
3. The app preprocesses the data and makes a prediction.
4. The result is displayed instantly.

---

## 🖥️ How to Run the App Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Himanwell/Diabetes-prediction-app.git
cd Diabetes-prediction-app
2️⃣ Install Dependencies

Make sure you have Python installed, then install the requirements:
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run "Diabetes prediction web app.py"
Then open the URL shown in your terminal (usually http://localhost:8501
).
| File                                           | Description                                        |
| ---------------------------------------------- | -------------------------------------------------- |
| `Diabetes prediction web app.py`               | Streamlit app that runs the web interface          |
| `predictive system.py`                         | Simple script for testing predictions manually     |
| `Deploying_Diabetes_Prediction_ML_model.ipynb` | Jupyter notebook showing how the model was trained |
| `requirements.txt`                             | List of dependencies required to run the app       |
| `.gitignore`                                   | Prevents unwanted files from being uploaded        |

🧰 Technologies Used

Python

Streamlit

Scikit-learn

NumPy

Pandas

Pickle



🧑‍💻 Author

Himanwell
📧 ogunkoyaemmanuel2024@gmail.com
https://github.com/Himanwell
