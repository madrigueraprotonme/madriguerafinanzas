import streamlit as st
import requests
import os
from dotenv import load_dotenv
import stripe
load_dotenv()
API_URL="http://127.0.0.1:8000/"
STRIPE_PUBLIC_KEY=os.getenv("STRIPE_PUBLIC_KEY")
stripe.api_key=STRIPE_PUBLIC_KEY

with st.container():
    col1,col2,col3=st.columns([1,3,1])
    with col2:
        st.markdown(
            """ 
            <div style="text-align: center;">
                <h1>CURSO DE INVERISION</h1>
                <h2>Contenido del curso </h2>
                <p>Vas adquir una formacion para siempre, que se estructura en 6 modulos y donde el ritmo de aprendizaje lo marcas tu
                Puedes repasar y revisar los contenidos las veces que requieras.
                No requieres de conocimientos previos, apto para todas las edades y todas las personas
                Cuanto antes adquieras este conocimiento mucho mejor, antes podras hacer crecer tus ahorros
                No es lo mismo crecer ahorros a los 70 años que desde los 18 años.                
                </p>
                
            </div>
            """,
            unsafe_allow_html=True, 

        )
        
        cola,colb,colc=st.columns([4,4,1])
        with colb:
            comprar_curso=st.button("Comprar",type="primary")
        st.divider()
        st.markdown(
            """ 
            <div style="text-align: center;">
                <h2>Ademas del curso</h2>
                
            </div>
            """,
            unsafe_allow_html=True, 

        )
        with st.expander("Gratis por un año"):
            st.markdown(
                """
                <div style='text-align: center;'>
                    <h3>Detalles del curso 📘</h3>
                    <p>Aprende inversión desde cero, con ejemplos reales y prácticas guiadas.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        
        
        
        
        
        
        
    
        st.markdown(
            """ 
            <div style="text-align: center;">
                <h2>Programa del curso</h2>
                
            </div>
            """,
            unsafe_allow_html=True, 

        )
        
        
        with st.expander("Modulo1:Prepara tu menffte"):
            st.markdown(
                """
                <div style='text-align: center;'>
                    <h3>Detalles del curso 📘</h3>
                    <p>Aprende inversión desde cero, con ejemplos reales y prácticas guiadas.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with st.expander("Modulo1:Prepara tu mente"):
            st.write("Antes de empezar tienes que ponerte las gafas ccorrectas, te mostramos como tener una vision 360 de ti mismo, es muy importante el autocontrol a la hora de invertir y seguir el proceso al 100%")
                
        with st.expander("Modulo1:Prepara tu mente"):
            st.write("Antes de empezar tienes que ponerte las gafas ccorrectas, te mostramos como tener una vision 360 de ti mismo, es muy importante el autocontrol a la hora de invertir y seguir el proceso al 100%")
        with st.expander("Modulo1:Prepara tu mente"):
            st.write("Antes de empezar tienes que ponerte las gafas ccorrectas, te mostramos como tener una vision 360 de ti mismo, es muy importante el autocontrol a la hora de invertir y seguir el proceso al 100%")
                
        with st.expander("Modulo1:Prepara tu mente"):
            st.write("Antes de empezar tienes que ponerte las gafas ccorrectas, te mostramos como tener una vision 360 de ti mismo, es muy importante el autocontrol a la hora de invertir y seguir el proceso al 100%")
        
        with st.expander("Modulo1:Prepara tu mente"):
            st.write("Antes de empezar tienes que ponerte las gafas ccorrectas, te mostramos como tener una vision 360 de ti mismo, es muy importante el autocontrol a la hora de invertir y seguir el proceso al 100%")
                    

        

if comprar_curso:
    response=requests.post(f"{API_URL}/crear-pago")
    if response.status_code==200:
        st.success(f"Pago enviado:{response.json()}")
        checkout_url = response.json()["url"]
       
        st.markdown(f"[👉 Ir al pago]({checkout_url})", unsafe_allow_html=True)
        #le enviamos un usuario y una contraseña para el acceso login pendiente
    else:
        st.error(f"Error al enviar el pago:{response.text}")
 