import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Try getting key from environment (local .env)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# If not found, try getting from Streamlit secrets (cloud deployment)
if not GOOGLE_API_KEY:
    try:
        GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in .env or Streamlit secrets.")

# Sanitize key (remove potential accidental quotes or whitespace)
GOOGLE_API_KEY = GOOGLE_API_KEY.strip().strip("'").strip('"')

print(f"DEBUG: API Key found. Length: {len(GOOGLE_API_KEY)}")
print(f"DEBUG: Key starts with: {GOOGLE_API_KEY[:4]}...")
print(f"DEBUG: Key ends with: ...{GOOGLE_API_KEY[-4:]}")

genai.configure(api_key=GOOGLE_API_KEY)

# Model configuration
MODEL_NAME = "gemini-flash-latest" # Updated to a valid model
GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}
