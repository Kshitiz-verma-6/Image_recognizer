import streamlit as st
import numpy as np
import os
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array

st.set_page_config(page_title="Image Recognition", page_icon="📷", layout="centered")

@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

st.title("📷 Image Recognition App")
st.write("Upload an image to classify it using pre-trained MobileNetV2.")

uploaded_file = st.file_uploader("Upload an image (JPG / PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Predict Object"):
        resized_img = img.resize((224, 224))
        img_array = img_to_array(resized_img)
        img_batch = np.expand_dims(img_array, axis=0)
        processed_img = preprocess_input(img_batch)
        
        preds = model.predict(processed_img, verbose=0)
        decoded = decode_predictions(preds, top=5)[0]
        
        top_label, top_prob = decoded[0][1], decoded[0][2]
        st.success(f"**Top Prediction**: {top_label.replace('_', ' ').title()} ({top_prob * 100:.2f}%)")
        
        st.write("### Top-5 Predictions:")
        for _, label, prob in decoded:
            st.write(f"- **{label.replace('_', ' ').title()}**: {prob * 100:.2f}%")
