import pandas as pd
import yfinance as yf #yahoo finance
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.title('Sectores del índice S&P 500')
st.caption('Los componentes del S&P 500 se dividen en 11 sectores, según la actividad económica que cada una realiza. Habitualmente, cada sector evoluciona de distinta manera dependiendo del estado general de la economía.')
st.caption("XLB: Materiales, XLE: Energía, XLF: Financiero, XLI: Industrial, XLK: Tecnología de la información, XLU: Servicios públicos, XLV: Salud, XLY: Consumo discrecional, XLRE: Inmobiliario, XLC: Servicios de comunicación, XLP: Consumo básico")

dona = pd.read_csv('sectores.csv')

# Agrupo los datos por sector y cuento la cantidad de veces que aparece cada sector
sector_counts = dona.groupby('sector').size()

# Calculo los porcentajes de cada sector
sector_percentages = sector_counts * 100 / len(dona)

# Crear la gráfica de dona interactiva con Plotly Express
fig = px.pie(
    sector_percentages,
    values=sector_percentages.values,
    names=sector_percentages.index,
    hole=0.5,
    color_discrete_sequence=px.colors.qualitative.Dark2,
    title='Porcentaje de Sectores',
    template='plotly_dark'
)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig)

if st.checkbox('Mostrar Datos'):
    st.dataframe(dona)

st.markdown("***")

##### Comparacion del comportamieto de los sectores en conjunto

st.markdown("#### Comparación del comportamiento de los sectores")


# Agrupo los datos por sector
sectors = dona.groupby("sector")


# Lista para almacenar las figuras
figures = {}

# Iterar sobre los grupos de sectores
for name, sector in sectors:
    # Calcula los rendimientos diarios del sector
    returns = (sector['Close'] - sector['Close'].shift(1)) / sector['Close'].shift(1)
    # Calcula la volatilidad diaria del sector
    volatility = returns.rolling(window=20).std() * (252 ** 0.5)
    # Grafica los rendimientos diarios y la volatilidad diaria del sector con Plotly
    fig = px.line(sector, x='Date', y=['Close', 'Volume'], title=name, color_discrete_sequence=px.colors.qualitative.Dark2)
    fig.add_scatter(x=sector['Date'], y=volatility, name='Volatilidad')
    # Agrega la figura al diccionario
    figures[name] = fig

# Muestra los botones para seleccionar el sector y mostrar la figura correspondiente
sector_selected = st.sidebar.selectbox('Selecciona un sector', list(figures.keys()))
st.plotly_chart(figures[sector_selected])



st.caption("La gráfica de rendimientos diarios muestra cómo varía el precio de cierre de cada sector en el S&P 500 de un día a otro, expresado como un porcentaje de cambio. Si el rendimiento diario es positivo, significa que el precio de cierre de ese día fue más alto que el del día anterior, y si es negativo, significa que el precio de cierre fue más bajo que el del día anterior.")
st.caption("La gráfica de volatilidad muestra cómo varía la variabilidad o dispersión de los rendimientos diarios de un sector en el S&P 500 a lo largo del tiempo, también expresado como un porcentaje de cambio. Una volatilidad alta significa que los precios de cierre de un sector están cambiando mucho de un día a otro, mientras que una volatilidad baja significa que los precios de cierre están cambiando poco.")
st.caption("Interpretando ambas gráficas juntas, se puede obtener una idea del riesgo y la rentabilidad de cada sector. Por ejemplo, un sector con un rendimiento diario alto y una volatilidad baja puede ser considerado menos riesgoso que un sector con un rendimiento diario bajo y una volatilidad alta. Sin embargo, es importante recordar que el rendimiento pasado no garantiza el rendimiento futuro, y que cada inversor debe considerar sus objetivos y tolerancia al riesgo antes de tomar decisiones de inversión.")

st.markdown("***")

st.markdown("#### Vamos a definir el sector más estable y con menos riesgo de inversión")
st.caption("Calculo la volatilidad anualizada promedio de cada sector y los ordeno de menor a mayor. El sector con la volatilidad más baja será considerado el más estable y con menos riesgo de inversión.")


# Leer los datos
dfc= pd.read_csv('sectores.csv')
# Agrupar por sector y calcular la volatilidad promedio anualizada
sectors = dfc.groupby("sector")
volatility = sectors.apply(lambda x: (x["Close"] - x["Close"].shift(1)) / x["Close"].shift(1)).rolling(window=20).std() * (252**0.5)
volatility = volatility.groupby("sector").mean()

# Ordenar los sectores por volatilidad de menor a mayor
volatility = volatility.sort_values()

# Crear la gráfica de barras horizontales con Plotly
fig = px.bar(volatility, x=volatility.values, y=volatility.index, orientation='h', color=volatility.values,
             color_continuous_scale=px.colors.qualitative.Dark2)

# Configurar el layout
fig.update_layout(
    title='Volatilidad promedio anualizada por sector',
    xaxis_title='Volatilidad',
    yaxis_title='Sector',
    margin=dict(l=0, r=0, t=50, b=0),
)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("###### El sector *XLV* que concierne a la Salud médica es el más estable en los últimos 23 años")

sect = """
**Sectores**:
- **XLB:** Materiales
- **XLE:** Energía
- **XLF:** Financiero
- **XLI:** Industrial
- **XLK:** Tecnología de la información
- **XLU:** Servicios públicos
- **XLV:** Salud
- **XLY:** Consumo discrecional
- **XLRE:** Inmobiliario
- **XLC:** Servicios de comunicación
- **XLP:** Consumo básico
"""
with st.sidebar.container():
    st.markdown(sect)
