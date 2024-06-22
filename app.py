import streamlit as st
import pandas as pd
import plotly.express as px

# Título del dashboard
st.title("Dashboard Interactivo de Delivery con Streamlit y Plotly")

# Cargar datos
@st.cache
def load_data():
    url = "data.csv"
    df = pd.read_csv(url, sep=';')  # Especificar el separador correcto
    return df

df = load_data()

# Mostrar los datos
st.write(df.head())  # Muestra las primeras filas del DataFrame para verificar las columnas

# Asegurarse de que las columnas 'fecha' y 'ventas' existen
if 'fecha' in df.columns and 'ventas' in df.columns:
    # Gráfica de ejemplo
    fig = px.line(df, x='fecha', y='ventas', title='Ventas a lo largo del tiempo')
    st.plotly_chart(fig)

    # Otras visualizaciones
    fig2 = px.pie(df, values='ventas', names='region', title='Ventas por región')
    st.plotly_chart(fig2)
else:
    st.error("Las columnas 'fecha' y 'ventas' no existen en el DataFrame.")
