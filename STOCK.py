import streamlit as st
import pandas as pd


def stock():
    st.title("Calculo del STOCK disponible de Gas")
    #lectura archivo stock onedrive
    def leer_excel(url, nombre_hoja):
        try:
            df = pd.read_excel(url, sheet_name=nombre_hoja)
            return df
        except Exception as e:
            st.error(f"Error al leer el archivo de Excel: {e}")

# URL del archivo Excel en OneDrive
    url_excel = 'https://enelcom.sharepoint.com/:x:/s/01_Planificacion_Operacion_Performance/EQqSXKLvyFJIkuNqMJIy7moBn0zSosbvoVJViu3KLLCsBA?e=S8NtcD'

# Nombre de la hoja que deseas leer
    nombre_hoja = "Stock Norte 24 Hrs"


# Título de la aplicación Streamlit
    st.title("Visualizador de Datos desde OneDrive")

# Leer el archivo de Excel desde OneDrive
    df = leer_excel(url_excel, nombre_hoja)

# Mostrar los datos en Streamlit
    if df is not None:
        st.write("Datos cargados exitosamente:")
        st.write(df)
    
    
