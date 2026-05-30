# 🌸 Iris Flower Classification using KNN

A Machine Learning based web application that predicts the species of an Iris flower using flower measurements.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)

---

# 📌 About The Project

The **Iris Flower Classification System** is a Machine Learning project that classifies Iris flowers into one of three species:

* 🌼 Iris Setosa
* 🌷 Iris Versicolor
* 🌺 Iris Virginica

The prediction is based on the following flower measurements:

* 📏 Sepal Length
* 📏 Sepal Width
* 📏 Petal Length
* 📏 Petal Width

The project uses a trained **K-Nearest Neighbors (KNN)** model and an interactive **Streamlit dashboard** for real-time predictions.

---

# 📑 Table of Contents

* ✨ Features
* 🛠️ Tech Stack
* 📂 Dataset
* 📸 Screenshots
* ⚙️ Installation
* 🚀 Usage
* 📁 Project Structure
* 📊 Model Performance
* 🎯 Learning Outcomes
* 👨‍💻 Author

---

# ✨ Features

* Iris flower species prediction

* Interactive Streamlit interface

* K-Nearest Neighbors (KNN) model

* Data visualization using Seaborn

* User input measurement graph

* Model saved using Joblib

* Real-time predictions

---

# 🛠️ Tech Stack

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Programming Language    |
| Pandas       | Data Processing         |
| NumPy        | Numerical Operations    |
| Matplotlib   | Data Visualization      |
| Seaborn      | Pair Plot Visualization |
| Scikit-Learn | Machine Learning        |
| Joblib       | Model Saving            |
| Streamlit    | Web Application         |

---

# 📂 Dataset

The Iris dataset contains **150 flower samples** divided into three classes.

### Features

| Feature       | Description  |
| ------------- | ------------ |
| SepalLengthCm | Sepal Length |
| SepalWidthCm  | Sepal Width  |
| PetalLengthCm | Petal Length |
| PetalWidthCm  | Petal Width  |

### Target

| Species         |
| --------------- |
| Iris-setosa     |
| Iris-versicolor |
| Iris-virginica  |

---

# 📸 Screenshots

### 🏠 Home Page 

![Home Page](images/Dashboard/dashboard.png)



## 📈 Graph / Visualization Output

![Home Page](images/Graph_Visulation/)



### 🌸 Prediction Result

```md
![Prediction](screenshots/prediction.png)
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Iris-Flower-Classification.git
cd Iris-Flower-Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run Iris.py
```

---

# 🚀 Usage

1. Enter flower measurements.
2. Click **Predict Species**.
3. View prediction results.
4. Analyze measurement graph.

---

# 📁 Project Structure

```text
Iris-Flower-Classification/
│
├── Iris.csv
├── notebook.ipynb
├── knn_model.pkl
├── Iris.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── home.png
    └── prediction.png
```

---

# 📊 Model Performance

### Algorithm Used

```python
KNeighborsClassifier(n_neighbors=3)
```

### Evaluation Metrics

* Accuracy Score
* Confusion Matrix
* Classification Report

### Sample Accuracy

```text
Accuracy: 96% - 100%
```

(depending on train-test split)

---

# 🎯 Learning Outcomes

This project helped in understanding:

* Supervised Machine Learning
* Classification Problems
* KNN Algorithm
* Data Visualization
* Model Evaluation
* Streamlit Deployment
* Model Serialization using Joblib

---

# 👨‍💻 Author

### Tarun Chahar

🎓 B.Tech Computer Science & Engineering Student

📚 Learning Data Science & Machine Learning

🔗 GitHub: Add your GitHub profile link here

---

## ⭐ If you like this project, consider giving it a star!
