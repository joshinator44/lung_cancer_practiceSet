import pandas as pd
import plotly.express as px
import streamlit as st
wheezing = []
cancer = 0
filename = "/Users/joshuata/Desktop/VisualStudio Code/lung_cancer/survey lung cancer.csv"
df = pd.read_csv(filename)
df = df.drop(columns = ["PEER_PRESSURE", "SHORTNESS OF BREATH", "YELLOW_FINGERS"])
male_cancer = 0
female_cancer = 0
for index, row in df.iterrows():
    if row["LUNG_CANCER"] == "YES":
        df.iat[index, 12] = 1
        cancer += 1
    else:
        df.iat[index, 12] = 0
for index, row in df.iterrows():
    if row["GENDER"] == "M":
        df.iat[index, 0] = 1
        if row["LUNG_CANCER"] == 1:
            male_cancer += 1
    else:
        df.iat[index, 0] = 0
        female_cancer += 1


print(cancer)
age_coughing = px.histogram(df["COUGHING"], x=df["AGE"])
st.dataframe(df)
st.set_page_config(page_title="Main Causes of Smoking")
st.header('What are the main causes and symptoms of Lung Cancer?')
print("Male cancer", str(male_cancer))
print("Female cancer", str(female_cancer))
