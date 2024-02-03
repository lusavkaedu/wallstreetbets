### import libraries
import numpy as np
import pandas as pd
import streamlit as st
import joblib
import source 
st.header('Sentiment Analysis of Amazon reviews')
st.subheader('Edo Spigel Emmerich')
st.subheader("Model")
choice = ["logistic-bal-model.pkl", "logistic-unbal-model.pkl", "decision-tree-bal-model.pkl", "decision-tree-unbal-model.pkl", "random-forest-unbal-model.pkl", "random-forest-bal-model.pkl"]

option = st.selectbox('Which model do you want to test out?',choice)

# Load the model using joblib
model = joblib.load(option)
# Set up input field with st.text_input()
st.write(f"Choice: {option}")
text = st.text_input("Enter your review here:", "Rubbish phone")

# Use the model to predict sentiment & save to a variable called prediction

prediciton = model.predict({text})
proba = model.predict_proba({text})[0]

# based on prediction display something to user
if prediciton == 1:
    st.write(f"Prediction: Positive!, Confidence: {proba[1]*100:.0f}")
else:
    st.write(f"Prediction: Negative!: Confidence: {proba[0]*100:.0f}%")

# vec = joblib.load("text_vectorizer.pkl")

transformed_text = model[0].transform([text])
feature_names = model[0].get_feature_names_out()
if option in ["logistic-bal-model.pkl", "logistic-unbal-model.pkl"]:
    coefficients = model[1].coef_[0]
    contributions = transformed_text.multiply(coefficients)
    contributions_dense = contributions.toarray().flatten()
    # feature contributions
    contributions_df = pd.DataFrame({
        'Feature': feature_names,  
        'Contribution': contributions_dense
    }).sort_values(by="Contribution",ascending=False)
    contributions_df['Feature'] = contributions_df['Feature'].str.replace(r'^.*gram__', '', regex=True)


    # contributions of features
    st.write("Feature contributions to the prediction:")
    st.dataframe(pd.concat([contributions_df.head(3), contributions_df.tail(3)], axis=0))
    # st.write(vec)
# elif option in ["random-forest-unbal-model.pkl", "random-forest-bal-model.pkl"]:
#     fi = model[1].feature_importances_
#     feature_contributions = pd.DataFrame(fi.reshape(1,-1), columns=feature_names, index=['Contribution']).T
#     sorted_contributions = feature_contributions.sort_values(by='Contribution', ascending=False)
#     st.write("Feature contributions to the prediction:")
#     st.dataframe(sorted_contributions.head(5))
