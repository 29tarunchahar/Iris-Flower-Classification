import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("knn_model.pkl")

# Page Title
st.title("🌸 Iris Flower Classification using KNN")

st.write("Enter flower measurements and predict the Iris species.")

# Input Fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    value=5.1,
    step=0.1
    
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    value=3.5,
    step=0.1
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    value=1.4,
    step=0.1
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    value=0.2,
    step=0.1
)

# Predict Button
if st.button("Predict Species"):

    # Create DataFrame from user input
    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm"
        ]
    )

    # Prediction
    prediction = model.predict(input_data)

    # Display Prediction
    st.success(f"🌸 Predicted Species: {prediction[0]}")

    # Graph Section
    st.subheader("📊 Entered Flower Measurements")

    features = [
        "Sepal Length",
        "Sepal Width",
        "Petal Length",
        "Petal Width"
    ]

    values = [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(features, values)

    ax.set_title("Flower Measurements")
    ax.set_ylabel("Length (cm)")

    st.pyplot(fig)
    


