import streamlit as st
import numpy as np
import pandas as pd
import joblib

with open('scaler.joblib','rb')as file:
    scale=joblib.load(file)
with open('final_model.joblib','rb')as file:
    model=joblib.load(file)
def prediction(input_list):
    scaled_input=scale.transform([input_list])
    pca_input=pca.transform(scaled_input)
    output=model.predict(pca_input)[0]
    if output==0:
        return 'Developed'
    elif output==1:
        return 'Underdeveloped'
    else:
        return 'Developing'
def main():
    st.title('HELP NGO FOUNDATION')
    st.subhead('this application will give the status of a country based on socio_economic and health')
    gdp=st.text_input('enter the GDP per population of a country')
    inc=st.text_input('enter the per capita income of a country')
    imp=st.text_input('enter the imports in terms of % of GDP')
    exp=st.text_input('enter the in the exports in terms of GDP')
    inf=st.text_input('enter the inflation rate in the country(%)')

    hel=st.text_input('enter the expenditure on heath in terms % of GDP')
    ch_m=st.text_input('enter the number of deaths for 1000 births for lessthan 5 years')
    fer=st.text_input('enter the average children born to a women in a country')
    if=st.text_input('enter the average life expectency in a country')

    in_data=[ch_m,exp,hel,imp,inc,if,fer,gdp]

    if st.button('predict'):
        response=prediction(in_data)
        st.success(response)
if __name__=='__main__':
    main()
        




