# Page Streamlit reconstruite de zéro pour prédiction
import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Titre de l'application
st.title("Voting intention prediction")
st.write("The system predicts if someone plans to vote, using their personal background data.")

# === 1. Chargement des données ===
@st.cache_data
def load_data():
    df = pd.read_csv("vote_intention_final.csv")
    df = df[df['vote_intention'].isin(['Yes', 'No'])].dropna()
    df['vote_intention'] = df['vote_intention'].map({'Yes': 1, 'No': 0})
    return df

df = load_data()

# === 2. Entraînement du modèle ===
X = pd.get_dummies(df.drop(columns='vote_intention'), drop_first=False)
y = df['vote_intention']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Sauvegarde (si nécessaire)
joblib.dump(model, "logisticAT.pkl")
pd.Series(X.columns).to_csv("logisticAT_features.csv", index=False)

# === 3. Interface utilisateur ===
age_options = ['18–24 years old', '25–34 years old', '35–44 years old', '45–54 years old', '55–64 years old', '65–74 years old', '75+ years old']
sex_options = ['Male', 'Female']
edu_options = ['Less than HS', 'High School', 'Some College', 'Bachelor+', 'Graduate+']
religion_options = ['Protestant', 'Catholic', 'Jewish', 'Other', 'None']
race_options = ['White', 'Black', 'Hispanic', 'Other']
interest_options = ['Interested', 'Not interested']
employment_options = ['Working', 'Unemployed', 'Retired', 'Student', 'Homemaker', 'Other']

age_group = st.selectbox("Age Group", age_options)
sex = st.selectbox("Gender", sex_options)
edu = st.selectbox("Education Level", edu_options)
religion = st.selectbox("Religion", religion_options)
race = st.selectbox("Ethnic Origin", race_options)
interest = st.selectbox("Political Interest", interest_options)
employment = st.selectbox("Employment Status", employment_options)

# Construction du DataFrame utilisateur
input_df = pd.DataFrame([{ 
    'age_group': age_group,
    'sex': sex,
    'education_level': edu,
    'religion_grouped': religion,
    'race_grouped': race,
    'political_interest': interest,
    'employment_status': employment
}])

input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

# Prédiction
if st.button("Vote choice prediction"):
    proba = model.predict_proba(input_encoded)[0][1]  # proba d’avoir l’intention de voter
    st.success(f"There is a {proba:.2%} probability of voting intention for this person.")
