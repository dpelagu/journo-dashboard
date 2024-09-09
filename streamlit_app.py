import pandas as pd
import streamlit as st

# URL pública del archivo de Google Sheets publicado como CSV
google_sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5IhZlfHc4GKJiLpR3b1TUYMGkpbt5iZ91aiMzcQBLi47D4Fb8IULD_opy4gnR1mA1w9pXDsXC5Dt9/pub?output=csv'

# Leer el archivo CSV directamente desde la URL
df = pd.read_csv(google_sheet_url)

# Mostrar los datos en Streamlit
st.write(df)
