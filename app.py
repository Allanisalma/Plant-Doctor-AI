import streamlit as st
st.set_page_config(page_title="Plant Doctor AI", page_icon=":seedling:", layout="wide")
st.title("Plant Doctor AI")
st.write("Welcome to Plant Doctor AI! This application helps you diagnose plant diseases and provides recommendations for treatment.")
st.subheader("Let's examine your plant's health.")
plant_name = st.text_input("Enter the name of your plant:")
plant_image = st.file_uploader("Upload an image of your plant:", type=["jpg", "jpeg", "png"])
if plant_name:
    st.write(f"plant name: {plant_name}")
if plant_image :
    st.image(plant_image, caption="Your plant, use_container__width=True")
    st.info("image uploaded successfully! " "AI analysis will be added next.")
