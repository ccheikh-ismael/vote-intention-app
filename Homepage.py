import streamlit as st

st.set_page_config(
    page_title="Home", 
    page_icon="👋", 
    layout="centered"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)


# Display logo
from PIL import Image
import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Center image using HTML + base64
img_base64 = get_base64_image("assets/logo.png")

st.markdown(
    f"""
    <div style='text-align: center; margin-bottom: 40px;'>
        <img src='data:image/png;base64,{img_base64}' width='200'/>
    </div>
    """,
    unsafe_allow_html=True
)


# User input
st.markdown(
    "<h5 style='text-align: center;'>Let's get started! What's your first name?</h5>",
    unsafe_allow_html=True
)

name = st.text_input("", placeholder="e.g. Alice")


if name:
    st.markdown(f"<h1 style='text-align: center;'>Hello {name} 👋</h1>", unsafe_allow_html=True)
    st.success("Use the left menu to navigate through the application.")

    # CONTINUE BUTTON
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 40px;">
            <a href="/Vote_Intention_Prediction" target="_self">
                <button style="
                    background-color: #007aff;
                    color: white;
                    padding: 12px 24px;
                    font-size: 16px;
                    border: none;
                    border-radius: 24px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    font-weight: 500;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                ">
                    Continue to prediction →
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )