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
                <h2>Bienvenido a nuestro programa de formacion </h2>
                <p><span style="color:rgb(255,75,75)">Aprenderas a invertir </span> en todo tipo de activo en bolsa, junto al colectivo de inversores, utilizando 
                nuestra sistema, que te permitirá invertir en bolsa de forma sencilla y segura.
                no esperes mas si quieres que tus ahorros no se devaluen con el paso del tiempo
                conoce los secretos y <span style="color:rgb(255,75,75)">alcanlza la libertad</span>                
                </p>
                
            </div>
            """,
            unsafe_allow_html=True, 

        )
        st.image("cabecera.jpg",width="stretch")
        cola,colb,colc=st.columns([4,4,1])
        with colb:
            ver_curso=st.button("Ver curso",type="primary")
if ver_curso:
    st.switch_page("pages/curso_detalle.py")
    

        


    