import streamlit as st
import pandas as pd

def Calculo_Vectores_GMetropolitana():
    st.title("Calculo Vectores Generadora Metropolitana")

    # Permitir que el usuario cargue un archivo Excel
    archivo_vector = st.file_uploader('Cargar archivo Excel Vectores Sistema', type= 'xlsx')

    #segunda archivo ADP
    # Permitir que el usuario cargue un archivo Excel
    archivo_ADP = st.file_uploader('Cargar archivo Excel ADP', type= 'xlsx')

    #tercer archivo descarga barco real
    # Permitir que el usuario cargue un archivo Excel
    archivo_descarga_barco = st.file_uploader('Cargar archivo Excel Descarga real Barcos', type= 'xlsx')
    
    # Verificar si se ha cargado un archivo
    if archivo_vector:
        st.markdown('---')
        try:
            # Leer el archivo Excel
            df = pd.read_excel(archivo_vector, engine='openpyxl',sheet_name='Demanda')
            
            # Mostrar los datos del archivo Excel
            st.write('**Datos del archivo Excel:**')
            st.write(df)
        
        except Exception as e:
            # Manejar posibles errores al cargar el archivo
            st.error(f'Ocurrió un error al cargar el archivo: {e}')



    
