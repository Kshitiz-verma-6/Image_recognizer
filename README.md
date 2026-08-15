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

### Why `NotFoundError: _kernel_dir` / `load_library` Occurs
In newer TensorFlow versions (2.16+), TensorFlow introduced Keras 3 and dynamic kernel C++ library loading. On headless cloud containers like Streamlit Cloud Linux instances, importing unpinned TensorFlow throws `NotFoundError: TF_LoadLibrary(_kernel_dir)` due to missing shared C++ ABI libraries and memory limits.

### Solution
1. **[`requirements.txt`](requirements.txt)**: Pins `tensorflow-cpu==2.15.0`. This CPU-optimized release includes stable static C++ bindings for Linux, uses ~150 MB RAM (well under Streamlit Cloud's 1 GB limit), and avoids dynamic kernel load errors.
2. **[`.python-version`](.python-version)** & **[`runtime.txt`](runtime.txt)**: Pins Python runtime to `3.11`, ensuring wheel compatibility.

### Deploying to Streamlit Cloud

1. Push your updated code to GitHub:
   ```bash
   git add requirements.txt .python-version runtime.txt README.md
   git commit -m "Pin tensorflow-cpu==2.15.0 to fix import load_library error"
   git push origin main
   ```
2. In the Streamlit Cloud dashboard ([share.streamlit.io](https://share.streamlit.io/)), click your app options menu (**⋮**) -> **Re-boot app**.

---

## 🔬 How it Works

1. **Image Preprocessing**: Uploaded images are converted to RGB, resized to `(224, 224)` pixels, converted to numpy arrays, and formatted into a 4D batch tensor (`(1, 224, 224, 3)`).
2. **Model Processing**: Inputs are scaled using `mobilenet_v2.preprocess_input` (scaling pixel values between -1 and 1) and fed through **MobileNetV2**.
3. **Prediction Decoding**: The raw prediction output vector of 1,000 probabilities is decoded using `decode_predictions` into human-readable class labels and confidence percentages.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
