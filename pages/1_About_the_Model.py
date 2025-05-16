import streamlit as st

st.title("📘 About This Application")

st.markdown("""
This application predicts an individual's **voting intention level** based on sociodemographic characteristics including:

- Age Group
- Gender
- Education level
- Religion
- Ethnic Origine
- Political interest
- Employment Status

The model uses **ordinal logistic regression** (`LogisticAT` model) trained on **ANES 2024** data from a U.S. electoral survey.

The goal is to provide an **interpretable** estimate useful for civic education or behavioral simulation.
""")