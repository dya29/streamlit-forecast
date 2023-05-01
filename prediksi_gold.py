import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksi_gold.sav','rb'))

df = pd.read_excel("MonthlyGoldPrice.xlsx")
df['Date'] = pd.to_datetime(df['Date'], format='%d%m%Y')
df.set_index(['Date'], inplace=True)

st.title('Forecasting Harga Gold')
year = st.slider("Tentukan Bulan",1,120, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['IDR'])

if st.button("Predict"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['IDR'].plot(style='--', color='gray', legend=True, label='known')
        pred['IDR'].plot(color='blue', legend=True, label='Prediction')
        st.pyplot(fig)