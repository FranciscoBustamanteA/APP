import streamlit as st
import pandas as pd
def Calculo_Vectores_GMetropolitana():
    st.title("Calculo Vectores Generadora Metropolitana")

# Permitir que el usuario cargue un archivo Excel
    archivo = st.file_uploader('Cargar archivo Excel', type=['xls', 'xlsx'])

# Intentar importar pandas con 'openpyxl'
    try:
        import pandas as pd
        from pandas import ExcelFile
        from pandas import ExcelWriter
    except ImportError:
        st.error("No se pudo importar pandas con openpyxl. Por favor, asegúrate de que pandas y openpyxl estén instalados.")
        st.stop()
    
# Verificar si se ha cargado un archivo
    if archivo is not None:
        try:
        # Leer el archivo Excel
            df = pd.read_excel(archivo)
        
        # Mostrar los datos del archivo Excel
            st.write('**Datos del archivo Excel:**')
            st.write(df)
        
        except Exception as e:
        # Manejar posibles errores al cargar el archivo
            st.error(f'Ocurrió un error al cargar el archivo: {e}')

    
