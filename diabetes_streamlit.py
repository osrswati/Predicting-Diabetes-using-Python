# Importing libraries
import pickle
import streamlit as st

# Load the trained model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Streamlit page
st.title('Prediction Diabetes') 

# Input fields for each feature

col1, col2 = st.columns(2)

with col1:
    st.subheader('Pregnancies')
    st.caption('Number of times pregnant')
    pregnancies = st.text_input('Input value pregnancies')

    st.subheader('BloodPressure')
    st.caption('Diastolic blood pressure (mm Hg)')
    blood_pressure = st.text_input('Input value blood pressure')

    st.subheader('BMI')
    st.caption('Body mass index (weight in kg/(height in m)^2)')
    bmi = st.text_input('Input value BMI')

    st.subheader('Diabetes Pedigree Function')
    st.caption('Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)')
    diabetes_pedigree_function = st.text_input('Input value diabetes pedigree function')

with col2:

    st.subheader('SkinThickness')
    st.caption('Triceps skin fold thickness (mm)')
    skin_thickness = st.text_input('Input value skin thickness')

    st.subheader('Insulin')
    st.caption('2-Hour serum insulin (mu U/ml)')
    insulin = st.text_input('Input value insulin')

    st.subheader('Age')
    st.caption('Age in years')
    age = st.text_input('Input your age')

    st.subheader('Glucose')
    st.caption('Plasma glucose concentration a 2 hours in an oral glucose tolerance test')
    glucose = st.text_input('Input value glucose')


# Prediction Test
if st.button('Test your potential to be diagnosed with diabetes'):
    # Convert input values to float and reshape into array
    features_values = [[float(pregnancies), float(glucose), float(blood_pressure), float(skin_thickness),
                        float(insulin), float(bmi), float(diabetes_pedigree_function), float(age)]]
    
    # Make prediction
    prediction = diabetes_model.predict(features_values)

    # Display result
    if prediction[0] == 0:
        result = 'Likely to have diabetes'
    else:
        result = 'Unlikely to have diabetes'
    
    st.success(result)