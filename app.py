import streamlit as st
import cv2
import pytesseract
from transformers import pipeline

st.set_page_config(page_title="AI Design Rater", layout="wide")

# Initialize model
@st.cache_resource
def load_model():
    return pipeline("image-to-text", model="llava-hf/llava-1.5-7b-hf")

llava = load_model()

# UI
st.title("📊 AI Design Quality Rater")
st.subheader("Upload an image of your table/graph for instant feedback")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display image
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
    with col2:
        with st.spinner("Analyzing design..."):
            # Process image
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            
            # Get feedback
            prompt = """Analyze this table/graph design and:
            1. Rate 1-10 on readability
            2. Check alignment, whitespace, fonts
            3. Suggest improvements"""
            
            feedback = llava(image, prompt=prompt)[0]["generated_text"]
            
            st.success("Analysis Complete!")
            st.subheader("Design Feedback")
            st.write(feedback)
            
            st.subheader("Extracted Text")
            st.text(text)