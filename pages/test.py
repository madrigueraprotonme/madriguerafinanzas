###################################
import streamlit as st
import pandas as pd
import requests
import datetime
#API_URL="http://127.0.0.1:8000/"
API_URL = "https://madriguerafinanzasbackend.onrender.com"

usuario_logueado=st.session_state["Usuario"]
st.subheader("Crear Usuario")
#formulario de entrada de datos.
with st.form("crear_usuario"):
    nombre=st.text_input("Nombre")
    edad=st.number_input("Edad")
    submit=st.form_submit_button("Crear")
    if submit:
        payload={"nombre":nombre,"edad":edad}
        response=requests.post(f"{API_URL}/usuarios/",json=payload)
        if response.status_code==200:
            st.success(f"Usuario creado:{response.json()}")
        else:
            st.error(f"Error al crear el usuario:{response.text}")



#mostramos la tabla 
st.subheader("mostrar usuarios")
response=requests.get(f"{API_URL}/usuarios/")
if response.status_code==200:
    usuarios=response.json()
    if usuarios:
        st.table(usuarios)
    else:
        st.info("no hay usuarios")
else:
    st.error("no se pudo cargar usuarios")
if st.button("Page 2"):
    st.switch_page("pages/dasboard.py")