# Nutritional Estimate App

This project allows users to upload meal images and get nutritional estimates using a Streamlit-based UI and our Computer Vision system.

A real-time nutrition feedback system that leverages computer vision and deep learning to estimate macronutrient content from food images. The solution integrates food recognition and portion estimation, aimed at helping users make informed dietary decisions with minimal manual input. Built using EfficientNetV2-S for feature extraction and prediction, the system is trained on the Nutrition-5k dataset and further optimized with hyperparameter tuning and multi-branch regression.

The pipeline begins with image classification to identify food types using fine-tuned EfficientNetV2-S, selected based on comparative analysis against other architectures. Once identified, the same feature extractor feeds into regression heads that predict protein, fat, carbohydrate, and mass values using normalized data and mean squared error loss. Depth and portion estimation techniques are also explored, adjusting for real-world camera angle variations. A basic interface using Streamlit presents the predictions to the user in an accessible format, offering immediate nutritional breakdown per dish. Together, these components form a scalable, data-driven approach to nutritional awareness and ultimately a more healthier society. 

Project done in Term 7 SUTD - 2024

---

## Features

-   **Upload Meal Photos**: Users can upload images of their meals.
-   **AI Analysis**: The app sends the uploaded image to a backend model for nutritional analysis.
-   **Nutritional Estimates**: Displays the analyzed image and provides a breakdown of key nutritional values.

---

## Setup Instructions

Follow these steps to set up the project on your local machine.

[Do note that your setup must be GPU enabled (e.g. cuda)]

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

---

### 2. Set Up a Virtual Environment

Create a Python virtual environment to manage dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment:

-   **Windows**:
    ```bash
    .venv\Scripts\activate
    ```
-   **macOS/Linux**:
    ```bash
    source .venv/bin/activate
    ```

Ensure your device is GPU enabled (e.g. cuda).

---

### 3. Install Dependencies

Install all required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
pip install openmim
mim install mmengine
mim install mmcv
```

---

### 4. Run the Streamlit App

Launch the Streamlit app:

```bash
streamlit run app.py
```

-   This will open the app in your default web browser.
-   If it doesn’t open automatically, navigate to the URL shown in the terminal (e.g. `http://localhost:8501`).

---

---

## About

This app is built using:

-   [Streamlit](https://streamlit.io/) for the UI.
-   Python 3.8+ for development.
-   Backend API to handle AI-based nutritional analysis.
