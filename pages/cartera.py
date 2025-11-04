import streamlit as st
import pandas as pd
import requests
import datetime
API_URL="http://127.0.0.1:8000/"
usuario_logueado=st.session_state["Usuario"]

st.title("📊 Cartera")
capital=st.session_state["capital_inicial"]

#primeros clolumans para el dasboard
col1,col2,col3=st.columns(3)

with col1:
    
    st.metric("Capital inicial",st.session_state["capital_inicial"],border=True)
with col2:
    st.metric("Capital real",0,border=True)
with col3:
    st.metric("efectivo",0,border=True)
    





#definimos dos columnas para 
col1,col2=st.columns([3,1])



with col2:
    with st.container(border=True):
        
        st.subheader("Añadir una nueva accion")
        st.badge("Para Anadir rellenar todos los campos",icon=":material/check:",color="blue")
        cola,colb=st.columns([1,1])
        
    
    with cola:
     
          
        nombre_accion=st.text_input("Nombre_accion")
        fecha_compra=st.date_input("fecha",value=datetime.date.today())
        fecha_compra=fecha_compra.isoformat()
        #capital=st.number_input("capital",value=10000,step=100)
        riesgo_operacion=st.number_input("riesgo operacion %",value=2.0, step=0.10)

        
        precio_compra=st.number_input("precio compra",value=10.0,step=0.10)
        precio_venta=st.number_input("precio venta",value=1.0)
        
        
        
        acciones_comprar=(capital*(riesgo_operacion/100))/(precio_compra-precio_venta)
        inversion=precio_compra*acciones_comprar
        liquidacion=precio_venta*acciones_comprar
        
        
    
        
        submit=st.button("Añadir a Cartera")
        if submit:
            payload={
                "nombre_accion":nombre_accion,
                "fecha_compra":fecha_compra,
                "capital":capital,
                "riesgo_operacion":riesgo_operacion,
                
                "precio_compra":precio_compra,
                "precio_venta":precio_venta,
                "acciones_comprar":acciones_comprar,
                "inversion":inversion,
                "liquidacion":liquidacion,
                "usuario_id":usuario_logueado                    }
            response=requests.post(f"{API_URL}/usuarios/cartera",json=payload)
            if response.status_code==200:
                st.success("Accion añadida")
            else:
                st.error(f"Error al crear la accion:{response.text}")
    
with col1:
    
 
    #dibujo la consulta
    with st.container(border=True, height="stretch"):
        
      
        
        st.subheader("Mostrar cartera por usuario")
        st.badge("Para modificar o eliminar selecciona el numero de indice",icon=":material/check:",color="blue")
        response=requests.get(f"{API_URL}/usuarios/{usuario_logueado }/cartera/")
        if response.status_code==200:
            carteras=response.json()
        #pasamos la respuesta a un dataframe de pandas
        
            event=st.dataframe(carteras,hide_index=False,on_select="rerun",selection_mode="single-row",width="content")
        else:
            st.info("no hay carteras")
    
    
    #eliminaos uusairos
    
        st.button("Eliminar")
        st.write(event.selection.rows)
    if event.selection.rows:
        fila=event.selection.rows[0]
 
       
        id_eliminar=carteras[fila]["id"]
        st.write(id_eliminar)
        response=requests.delete(f"{API_URL}/usuarios/cartera/{id_eliminar}")
        if response.status_code==200:
            st.success(f"Eliminado:{response.json()}")
        else:
            st.error(f"Error al eliminar la accion:{response.text}")

      




