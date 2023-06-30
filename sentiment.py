import streamlit as st
from transformers import pipeline

# Set page configuration
st.set_page_config(page_title="Sentiment Analysis", page_icon="😳😢")

# Set page layout
st.title("Sentiment Analysis")
st.markdown("---")

# Create pipeline
pipe = pipeline('sentiment-analysis')

# Text input
text = st.text_area('Enter text')

if text:
    st.markdown("---")
    # Run sentiment analysis
    out = pipe(text)
    label = out[0]['label']
    score = out[0]['score']
    
    # Display results
    st.subheader("Sentiment Analysis Result")
    st.write(f"Label: {label}")
    st.write(f"Score: {score}")
