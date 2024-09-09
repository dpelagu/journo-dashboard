import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv('metricas.csv')  # Si lo guardaste como CSV
# Si usas API:
# df = pd.read_json('URL_DE_LA_API')

st.title('Dashboard Journo')

# Mostrar los datos en tabla
st.write(df)

# Crear gráfico con seaborn o matplotlib
st.subheader('Gráfico de Métricas')
fig, ax = plt.subplots()
sns.lineplot(data=df, ax=ax)
st.pyplot(fig)

