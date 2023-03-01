import pandas as pd
import yfinance as yf #yahoo finance
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.markdown("#### Ya que tenemos el sector más estable, vamos a analizarlo y saber cuales empresas nos conviene hacer la inversión")

st.markdown("## KPI")
st.caption("_(Key Performance Indicator)_")
st.caption("En español es el Indicador Clave de Desempeño o Medidor de Desempeño, hace referencia a una serie de métricas que se utilizan para sintetizar la información sobre la eficacia y productividad de las acciones que se lleven a cabo en un negocio con el fin de poder tomar decisiones y determinar aquellas que han sido más efectivas a la hora de cumplir con los objetivos marcados en un proceso o proyecto concreto.")
st.caption("Los KPIs no sólo te permiten determinar los resultados para una acción o estrategia concreta, sino que además ofrecen una visión global de la situación, ya que facilitan la determinación de puntos fuertes y débiles (aspectos de mejora) en las inversiones.")
st.markdown("###### Estos KPIs nos ayudarán tomar una decisión informada al elegir las empresas correctas para invertir")

# Llamar el archivo antes guardado para trabajar en local
df_sector_xlv1 = pd.read_csv('sector_xlv.csv')

################## KPI 1
st.markdown("###### 1. Rendimiento total:")
st.caption(" Es una medida simple del rendimiento de una inversión que tiene en cuenta tanto la apreciación del precio de las acciones como cualquier dividendo pagado. El rendimiento total se define como:")
st.caption("Rendimiento total = (Precio de cierre ajustado final - Precio de cierre ajustado inicial + Dividendos) / Precio de cierre ajustado inicial.")

# Calcula el retorno total acumulado para cada símbolo con groupby
df_sector_xlv1['Precio Inicial'] = df_sector_xlv1.groupby('Symbol')['Open'].transform('first')
df_sector_xlv1['Precio Final'] = df_sector_xlv1.groupby('Symbol')['Close'].transform('last')
df_sector_xlv1['Retorno Total Acumulado'] = (df_sector_xlv1['Precio Final'] / df_sector_xlv1['Precio Inicial']) - 1

# Crea una figura con Plotly Express
fig = px.bar(
    df_sector_xlv1.groupby('Symbol')['Retorno Total Acumulado'].last().reset_index(),
    x='Symbol',
    y='Retorno Total Acumulado',
    title='KPI de Rendimiento Total',
    color='Symbol',
    color_discrete_sequence=px.colors.qualitative.Dark2
)

# Agrega la figura a Streamlit
st.plotly_chart(fig)

# Conclusión KPI 1

texto1 = """
Las 3 empresas con mejor rendimiento son:
1. **ISRG** Intuitive Surgical, Inc.
2. **SIDXX** Laboratories, Inc.
3. **UNH** UnitedHealth Group Incorporated
"""
st.markdown(texto1)

st.markdown('***')

################ KPI 2
st.markdown("###### 2. Volatilidad")
st.caption("  Es una medida de la variabilidad del precio de las acciones. Una empresa con una volatilidad alta puede ser más riesgosa que una empresa con una volatilidad baja. La fórmula para la volatilidad es:")
st.caption("Volatilidad = Desviación Estándar de los Precios de Cierre")


# Calcula la volatilidad para cada símbolo con groupby
df_sector_xlv1['Volatilidad'] = df_sector_xlv1.groupby('Symbol')['Close'].transform('std')

# Crear el gráfico con Plotly Express
fig = px.bar(df_sector_xlv1.groupby('Symbol')['Volatilidad'].last().reset_index(), 
             x='Symbol', y='Volatilidad', 
             title='KPI de Volatilidad',
             color='Symbol',
             color_discrete_sequence=px.colors.qualitative.Dark2)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Conclusión KPI 1

texto2 = """
Las empresas con menor volatibilidad son:
1. **PFE** Pfizer Inc.
2. **BMY** Bristol-Myers Squibb Company
3. **MRK** Merck & Co. Inc.

"""
st.markdown(texto2)

st.markdown('***')

################ KPI 3
st.markdown("###### 3. Ratio Precio-Ganancias")
st.caption("Es una medida de la valuación relativa de una empresa en el mercado de acciones. Puede indicar si una empresa está sobrevalorada o subvaluada en comparación con sus pares. La fórmula para el P/E Ratio es:")
st.caption("P/E Ratio = Precio Actual de las Acciones / Ganancias Por Acción (EPS)")

# Calcula el P/E Ratio para cada símbolo con groupby
df_sector_xlv1['P/E Ratio'] = df_sector_xlv1['Close'] / df_sector_xlv1.groupby('Symbol')['Close'].transform('mean')

# Crear el gráfico con Plotly Express
fig = px.bar(df_sector_xlv1.groupby('Symbol')['P/E Ratio'].last().reset_index(), 
             x='Symbol', y='P/E Ratio', 
             title='KPI de P/E Ratio',
             color='Symbol',
             color_discrete_sequence=px.colors.qualitative.Dark2)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

texto3 = """
Las empresas con ratio mas elevado, o que tengan mejor ganancia por cada acción son:
1. **UNH** UnitedHealth Group Incorporated
2. **LLY** Eli Lilly and Company
3. **TMO** Thermo Fisher Scientific Inc.

"""
st.markdown(texto3)

st.markdown('***')


##############  TOP 3 ###############

tOP3 = """
Con este análisis se puede concluir que las mejores empresas para invertir a largo plazo son:
1. **UnitedHealth Group** (UNH)
2. **Humana** (HUM)
3. **Pfizer** (PFE) 
"""
if st.button("Mostrar top 3"):
    st.markdown(tOP3)


if st.checkbox('Ojo'):
    st.markdown("[Wall Street](https://www.estrategiasdeinversion.com/actualidad/noticias/bolsa-eeuu/dos-acciones-del-sector-de-la-salud-con-compra-n-581039)")


# Empresas sidebar
empresas = """
- **JNJ:** Johnson & Johnson
- **UNH:** UnitedHealth Group
- **PFE:** Pfizer Incorporated
- **MRK:** Merck & Co. Inc.
- **ABT:** Abbott Laboratories
- **TMO:** Thermo Fisher Scientific Inc.
- **MDT:** SMedtronic plc
- **AMGN:** Amgen Inc.
- **ABBV:** AbbVie Inc.
- **BMY:** Bristol-Myers Squibb Company
- **CVS:** CVS Health Corporation
- **ANTM:** Anthem Inc.
- **GILD:** Gilead Sciences Inc.
- **CI:** The Cigna Group
- **ISRG:** Intuitive Surgical Inc.
- **DHR:** Danaher Corporation
- **SYK:** Stryker Corporation
- **VRTX:** Vertex Pharmaceuticals Inc.
- **BIIB:** Biogen Inc.
- **LLY:** Eli Lilly and Company
- **BDX:** Becton, Dickinson and Company
- **HCA:** HCA Healthcare Inc.
- **ZBH:** Zimmer Biomet Holdings, Inc.
- **REGN:** Regeneron Pharmaceuticals
- **HUM:** Humana Inc.
- **IDXX:** IDEXX Laboratories, Inc.
- **EW:** Edwards Lifesciences Co.
- **ALGN:** Align Technology, Inc.
- **BAX:** Baxter International Inc.
- **ILMN:** Illumina Inc.
- **LH:** Lab. Co. America Holdings
"""
with st.sidebar.container():
    if st.checkbox('Empresas XLV'):
        st.markdown(empresas)



