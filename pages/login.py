import streamlit as st
import requests
import pandas as pd
API_URL="http://127.0.0.1:8000/"
st.header("Loggin")

usuario=st.text_input("Usuario")
edad_texto=st.text_input("Edad",value=0,type="password")
##para que no de errores tenemos que ver que la edad tenga siempre un valor
if edad_texto:
    try:
        edad=int(edad_texto)
    except:
        st.error("Ingresa tu edad")
#tomamos toda la tabla de usuarios.
response=requests.get(f"{API_URL}/usuarios/")
if response.status_code==200:
    usuarios=response.json()
    df=pd.DataFrame(usuarios)
    if usuarios:
        st.table(usuarios)
    else:
        st.info("no hay usuarios")
else:
    st.error("no se pudo cargar usuarios")

st.write(usuario)
#nombre_encontrado=df[df['nombre']==usuario][['nombre']]
buscar_columna_nombre=df['nombre'].values
buscar_columna_edad=df['edad'].values
if st.button("Login"):
    if usuario in buscar_columna_nombre:
        
        if edad in buscar_columna_edad:
            st.session_state["Usuario"]=usuario
            st.session_state["Edad"]=edad
        
            st.session_state["logged_in"]=True
            st.session_state["exito"]=True
            payload={
                "usuario_profile":usuario,
                "edad":edad,
                "riesgo_global_profile":0,
                "riesgo_operacion_profile":0,
                "capital_inicial_profile":10000 
            }
            request=requests.get(f"{API_URL}/profile/{usuario}")
            data=request.json()
            if data:
                
                datos=True
            else:
                requests.post(f"{API_URL}/profile/",json=payload)
            st.rerun()
        
        else:
            st.error("Edad no correcta")
            
        
        
    else:
        st.error("Usuario no encontrado")
        st.session_state["Usuario"]=""
        st.session_state["Edad"]="0"

st.write(st.session_state)
#valor=st.button("Login")
#st.write(valor)∫
#if valor==True:
    #st.session_state["logged_in"]=True  
