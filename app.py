import streamlit as st
import pandas as pd
import pickle

st.image("http://www.ehtp.ac.ma/images/lo.png")
st.write("""
# MSDE4 : ML Project
## Price Diabet Prediction App

This app predicts the **Price Diabet** 
""")

st.sidebar.image("image2.jpeg",width=300)

option = st.selectbox(
     'How would you like to use the prediction model?',
     ('','Diabet Prediction real-time', 'Diabet Prediction Model'))

def user_input_features():
    Pregnancies = st.number_input("Pregnancies",value=0.0,format='%f',step=1.0)
    Glucose = st.number_input("Glucose",value=0.0,format='%f',step=1.0)
    BloodPressure = st.number_input("BloodPressure",value=0.0,format='%f',step=1.0) 
    SkinThickness = st.number_input("SkinThickness",value=0.0,format='%f',step=1.0)  
    Insulin = st.number_input("Insulin",value=0.0,format='%f',step=1.0)   
    BMI = st.number_input("BMI",value=0.0,format='%f',step=1.0) 
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",value=0.0,format='%f',step=1.0)  
    Age = st.number_input("Age",value=0.0,format='%f',step=1.0) 
 
        
    data = {'Pregnancies': Pregnancies,
            'Glucose': Glucose,
            'BloodPressure': BloodPressure,
            'SkinThickness': SkinThickness,
            'Insulin': Insulin,
            'BMI': BMI,
            'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
            'Age': Age
                                  }
    features = pd.DataFrame(data, index=[0])
    return features


def show_results():
    st.subheader(" Input parameters")
    st.write(price)
    model_price = pickle.load(open("model.pkl", "rb"))
    prediction = model_price.predict(price)
    st.subheader("Prediction")
    prediction_proba = model_price.predict_proba(price)
    st.subheader('Class labels and their corresponding index number')
    st.write(pd.DataFrame(model_price.classes_))

    st.subheader('Prediction')
    st.write(prediction)

    st.subheader('Prediction Probability')
    st.write(prediction_proba)



if option=='Diabet Prediction real-time':
    st.sidebar.header('User Input Parameters')
    price = user_input_features()
    show_results()


#if option=='Diabet Prediction Model':
 #   
 #  uploaded_file = st.file_uploader("Choose a file to load")
 # if uploaded_file is not None:
 #       df = pd.read_csv(uploaded_file)
 # 
 #     st.write(df)
 #
 #      model_loan=pickle.load(open("model.pkl", "rb"))
 #
 #       if st.button('Predict'):
 #           prediction = model_loan.predict(df)
 #           df["Prediction"] = prediction
 #           st.balloons()
 #           st.write(df)
 #   else:
 #       st.error("please try some prediction, then the data will be available here")
        
        
