import pandas as pd
import yfinance as yf #yahoo finance
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.sidebar.image('paradoja-2.png')

st.markdown('## Asesoría de inversión en el mercado bursatil')

st.image('artist-bubbles.png')
st.markdown('***')# Hace una línea

st.subheader('S&P 500')
st.caption("_(Standard and Poor's 500)_")
st.caption("El índice Standard & Poor's 500 (Standard & Poor's 500 Index), también conocido como S&P 500, es uno de los índices bursátiles más importantes de Estados Unidos. Al S&P 500 se lo considera el índice más representativo de la situación real del mercado.")



#Define un objeto ticker para el índice SP500 utilizando yfinance:
tickerSymbol = '^GSPC'
tickerData = yf.Ticker(tickerSymbol)


#st.dataframe(tickerDf) # Muestra el Df

#Obtén el histórico de precios del índice SP500 utilizando el método history de yfinance:
tickerDf = tickerData.history(period='1d', start='2000-1-1', end='2023-2-23')

# problema de fecha con plotly
tickerDf.reset_index(inplace=True)  # resetear el índice del DataFrame
tickerDf.rename(columns={'index': 'Date'}, inplace=True)  # renombrar la columna de fecha

#Analizar los datos obtenidos con pandas, retorno diario del índice
tickerDf['Daily Return'] = tickerDf['Close'].pct_change()

# Creamos la gráfica con plotly
fig = px.line(tickerDf, x='Date', y='Close')

st.markdown('***')# Hace una línea

# Agregamos título y etiquetas de los ejes
fig.update_layout(title='Gráfico de precios de cierre del índice S&P 500')
fig.update_xaxes(title='Fecha')
fig.update_yaxes(title='Precio de cierre')

# # Mostramos la gráfica en Streamlit
st.plotly_chart(fig)

df_in = pd.read_csv('data_grupo.csv')
if st.checkbox('Mostrar Datos'):
    st.dataframe(df_in)

