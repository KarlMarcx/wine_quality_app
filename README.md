# 🍷 Boutique Winery – Wine Quality Predictor

A Streamlit-based machine learning application that predicts whether a wine is **Good** or **Not Good** based on its physicochemical properties.

The model uses a trained Scikit-learn pipeline to classify wine samples and provides a confidence score for each prediction.

---

## Features

- Interactive web interface built with Streamlit
- Predicts wine quality in real time
- Displays prediction confidence
- Uses a pre-trained machine learning pipeline
- Simple and lightweight deployment

---

## How It Works

The application accepts the following wine characteristics as input:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

After submission, the model classifies the wine as:

- **GOOD** (quality ≥ 7)
- **NOT GOOD** (quality < 7)

and displays the corresponding confidence score.

---

## Project Structure

```text
wine_quality_app/
│
├── streamlit_app.py              # Main Streamlit application
├── wine_quality_pipeline.joblib  # Trained ML pipeline
├── metadata.joblib              # Feature metadata
├── requirements.txt             # Project dependencies
└── .devcontainer/               # Development container configuration
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KarlMarcx/wine_quality_app.git
cd wine_quality_app
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run streamlit_app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## Dependencies

- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

Install them manually if needed:

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

---

## Example Usage

1. Launch the application.
2. Enter the physicochemical properties of a wine sample.
3. Click **Predict**.
4. View:
   - Prediction result (**GOOD** or **NOT GOOD**)
   - Model confidence score

---

## Machine Learning Model

The application loads a serialized Scikit-learn pipeline from:

```text
wine_quality_pipeline.joblib
```

Metadata, including feature names and target labels, is loaded from:

```text
metadata.joblib
```

Target mapping:

| Label | Value |
|---------|---------|
| GOOD | 1 |
| NOT GOOD | 0 |

---

## Future Improvements

- Support for multiclass quality prediction
- Feature importance visualization
- Batch prediction through CSV upload
- Model performance dashboard
- Cloud deployment

---

## Author

**Karl Marcx**

GitHub: https://github.com/KarlMarcx

---

## License

This project is intended for educational and academic purposes.
