import streamlit as st
import requests
import pandas as pd
API_URL="http://127.0.0.1:8000/"
st.header("Mi perfil")


col1,col2=st.columns([1,2],gap="large")

with col1:
    with st.container(border=True):
        
        st.subheader("Seguridad")
        with st.expander("Tus datos de Login"):
            
            
            st.write(st.session_state["Usuario"])
            st.write(st.session_state["Edad"])
        
       
         
            

    with st.container(border=True):
        st.subheader("Gestion de Cartera")
        with st.expander("Gestion de Riesgo %"):
            st.session_state["riesgo_global"]=st.slider("Riesgo Global",0,10,value=0,format="%d%%", width=300)
            st.session_state["riesgo_operacion"]=st.slider("Riesgo por operacion",0,10,value=0,format="%d%%",width=300)
            colz,coly=st.columns([3,1])
            with coly:
                actualizar_gestion_cartera=st.button("Actualizar",type="primary",key="1")

    with st.container(border=True):
        st.subheader("Capital")
        with st.expander("Capital inicial"):
            st.session_state["capital_inicial"]=st.number_input("Capital inicial",step=100,value=10000,width=300)
            cola,colb=st.columns([3,1])
            with colb:
                capital_inicial_setting=st.button("Actualizar",key="2",type="primary")            

#muestro si hay configuracion
with col2:
    if st.session_state["exito"]==True:
        request=requests.get(f"{API_URL}/profile/{st.session_state['Usuario']}")
        if request.status_code==200:
            perfil=request.json()
            colg,colh,coli=st.columns(3,gap="small")
            with colg:
            
                
                st.metric("Capital inicial",perfil[0]["capital_inicial_profile"])
            with colh:    
                st.metric("Riesgo global",perfil[0]["riesgo_global_profile"])
            with coli:
                st.metric("Riesgo operacion",perfil[0]["riesgo_operacion_profile"])
        else:
            st.error(f"Error al obtener el perfil:{request.text}")

                    
    if capital_inicial_setting or actualizar_gestion_cartera:
        payload={
            "usuario_profile":st.session_state["Usuario"],
            "edad":st.session_state["Edad"],
            "riesgo_global_profile":st.session_state["riesgo_global"],
            "riesgo_operacion_profile":st.session_state["riesgo_operacion"],
            "capital_inicial_profile":st.session_state["capital_inicial"]
        }
        response=requests.put(f"{API_URL}/profile/{st.session_state['Usuario']}",json=payload)
        
        if response.status_code==200:
            st.success(f"Actualizado:{response.json()}")
            st.session_state["exito"]=True
            
            
        else:
            st.error(f"Error al actualizar el perfil:{response.text}")  
        st.rerun()