import streamlit as st
import pandas as pd
from pandas_ai_engine import ask_ai

st.set_page_config(
    page_title="AI Data Chat Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Chat Dashboard")

st.markdown("Upload your dataset and chat with your data using AI.")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # Show dataframe
    st.subheader("📊 Dataset Preview")
    st.dataframe(df)

    # User question
    user_prompt = st.text_input(
        "Ask something about your data"
    )

    if st.button("Generate AI Response"):

        if user_prompt.strip() == "":
            st.warning("Please enter a question.")
        else:

            with st.spinner("AI is analyzing your data..."):

                try:
                    response = ask_ai(df, user_prompt)

                    st.subheader("✅ AI Response")
                    st.write(response)

                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("Please upload a dataset to continue.")
