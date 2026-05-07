import os
from dotenv import load_dotenv
from pandasai import SmartDataframe
from langchain_groq import ChatGroq

load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def ask_ai(df, prompt):

    smart_df = SmartDataframe(
        df,
        config={
            "llm": llm,
            "verbose": True,
            "save_charts": True
        }
    )

    response = smart_df.chat(prompt)

    return response
