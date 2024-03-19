import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def stock():
    st.title("Calculo del STOCK disponible de Gas")
    #lectura archivo stock onedrive
    def leer_excel(url, nombre_hoja, columnas):
        try:
            df = pd.read_excel(url, sheet_name=nombre_hoja, usecols=columnas)
            return df
        except Exception as e:
            st.error(f"Error al leer el archivo de Excel: {e}")

# URL del archivo Excel en OneDrive
    url_excel = https://enelcom.sharepoint.com/:x:/r/sites/01_Planificacion_Operacion_Performance/_layouts/15/Doc.aspx?sourcedoc=%7BA25C920A-C8EF-4852-92E3-6A309232EE6A%7D&file=Stock%20GNL%202022%20F%20V2.xlsx&action=default&mobileredirect=true

# Nombre de la hoja que deseas leer
    nombre_hoja = "Stock Norte 24 Hrs"


# Título de la aplicación Streamlit
    st.title("Visualizador de Datos desde OneDrive")

# Leer el archivo de Excel desde OneDrive
    df = leer_excel(url_excel, nombre_hoja, columnas_especificas)

# Mostrar los datos en Streamlit
    if df is not None:
        st.write("Datos cargados exitosamente:")
        st.write(df)
    
    
