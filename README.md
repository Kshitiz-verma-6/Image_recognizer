# 📷 Image Recognition App

An interactive Machine Learning web application built with **Streamlit** and **TensorFlow / Keras**. This application leverages transfer learning with a pre-trained **MobileNetV2** model trained on the ImageNet dataset (1,000 object classes) to instantly classify user-uploaded images and present top-5 predictions with confidence scores.

---

## ✨ Features

- 🖼️ **Easy Image Upload**: Upload any image file (`.jpg`, `.jpeg`, `.png`) for real-time classification.
- 🧠 **Deep Learning Backbone**: Powered by Google's lightweight and efficient **MobileNetV2** architecture.
- 📊 **Top-5 Class Predictions**: Displays the single most likely object class along with a detailed top-5 breakdown and confidence percentages.
- ⚡ **Cached Model Loading**: Uses `@st.cache_resource` to load the deep learning model once into memory for ultra-fast predictions.
- 🚀 **Cloud Deployment Ready**: Optimized for seamless deployment on **Streamlit Community Cloud**.
- 📓 **Notebook Walkthrough**: Includes a complete Jupyter Notebook ([`image_recognition.ipynb`](image_recognition.ipynb)) demonstrating data preprocessing, batch dimension expansion, and prediction decoding step by step.

---

## 🛠️ Project Structure

```text
Image_recognizer/
├── app.py                   # Main Streamlit web application
├── image_recognition.ipynb  # Jupyter Notebook with step-by-step walkthrough
├── sample_image.jpg         # Sample image for testing classification
├── requirements.txt         # Python package dependencies
├── runtime.txt              # Specifies Python 3.11 runtime for Streamlit Cloud
├── .python-version          # Specifies Python 3.11 for uv dependency resolver
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or 3.11 installed on your system.
- Git installed on your system.

### Local Installation & Running

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/Image_recognizer.git
   cd Image_recognizer
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**
   - **On macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **On Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit App**
   ```bash
   streamlit run app.py
   ```
   The app will automatically open in your default browser at `http://localhost:8501`.

---

## 🌐 Streamlit Cloud Deployment Fix

If you encountered dependency resolution errors when deploying to Streamlit Community Cloud (e.g. `Using Python 3.14.7 environment ... requirements are unsatisfiable` or `No matching distribution found for tensorflow`), follow these steps:

### Why the Error Happened
Streamlit Cloud's build runner uses `uv` and default base images that spin up with **Python 3.14.7**. Since TensorFlow binary wheels do not exist for Python 3.14 on PyPI, `uv` fails to resolve dependencies.

### How it is Fixed
1. **[`.python-version`](.python-version)**: Specifies `3.11`. `uv` reads this file to set the Python virtual environment version.
2. **[`runtime.txt`](runtime.txt)**: Specifies `python-3.11` for Streamlit Cloud's runtime manager.
3. **[`requirements.txt`](requirements.txt)**: Standardizes dependencies (`streamlit`, `tensorflow`, `numpy<2.0.0`, `pillow`).

### Deploying to Streamlit Cloud

1. Push your updated code to GitHub:
   ```bash
   git add .python-version runtime.txt requirements.txt README.md
   git commit -m "Fix Streamlit Cloud Python version and dependencies"
   git push origin main
   ```
2. Go to your app settings on [share.streamlit.io](https://share.streamlit.io/):
   - Click **Settings** (or ⚙️ icon next to your app).
   - Under **Advanced settings** -> **Python version**, select **3.11** (or 3.10).
   - Click **Save** and click **Re-deploy app**.

---

## 🔬 How it Works

1. **Image Preprocessing**: Uploaded images are converted to RGB, resized to `(224, 224)` pixels, converted to numpy arrays, and formatted into a 4D batch tensor (`(1, 224, 224, 3)`).
2. **Model Processing**: Inputs are scaled using `mobilenet_v2.preprocess_input` (scaling pixel values between -1 and 1) and fed through **MobileNetV2**.
3. **Prediction Decoding**: The raw prediction output vector of 1,000 probabilities is decoded using `decode_predictions` into human-readable class labels and confidence percentages.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
