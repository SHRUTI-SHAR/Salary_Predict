import joblib
import streamlit as st
st.set_page_config(page_title="My Salary Prediction Model",page_icon="🤓🤓")
st.title("Machine Learning Model Deployment")
st.write("""My *Salary Prediction* Model Vs Experience""")
mymodel=joblib.load("salary.pkl")

exp= st.sidebar.slider("Experience (In Years)",1.0,50.0,2.0)
salary= mymodel.predict([[exp]])
st.write(f"Experience-",exp)
st.write(f"Salary-",salary)
