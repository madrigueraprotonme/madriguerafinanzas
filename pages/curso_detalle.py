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
                <p>Vas adquir una formacion para siempre, que se estructura en <span style="color:rgb(255,75,75)">6 módulos online</span> y donde el ritmo de aprendizaje lo marcas tu.
                Puedes repasar y revisar los contenidos las veces que requieras.
                No requieres de conocimientos previos, apto para todas las edades 
                Cuanto antes adquieras este conocimiento mucho mejor, antes podras hacer crecer tus ahorros
                No es lo mismo hacer crecer los ahorros en tu final de vida que cuando terminas la univeridad o has creado tu familia..                
                Además del curso tendrás a <span style="color:rgb(255,75,75)">acceso gratuito por 3 meses </span>  a la plataforma de seleccion de los mejores activos y recursos
                </p>
                <br>
                <br>
               
            </div>
            """,
            unsafe_allow_html=True, 

        )
        cola,colb,colc=st.columns([4,4,1])
        with colb:
           
           
           
            
            comprar_curso=st.button("Comprar",type="primary")
            st.badge("Precio 299€",color="orange")
            st.write("")
        
        st.markdown(
            """ 
            <div style="text-align: center">
                <h2 style="text-color:rgb(255,75,75)" >Programa del curso</h2>
                <br>
            </div>
            """,
            unsafe_allow_html=True, 

        )
        
        with st.expander("Modulo1"):
            st.markdown(
                """
                <div style='text-align: left;'>
                    <h3>Prepara tu mentecuerpo 📘</h3>
                    <p>En este primer modulo te prepararas para  estar fresco e invertir con autocontrol, compites contra todos y tu cuerpo y tu mente tienen que estar sincronizados</p>
                    <hr>
                    <ol style="
                        display: inline-block;
                        text-align: left;
                        color: rgb(255,75,75);
                        list-style-position: inside;
                        padding-left: 0;
                    ">
                        <li>Introduccion</li>
                        <li>Metabolisbo para ganar</li>
                        <li>Actividad ganadora</li>
                        <li>Relaciones de poder</li>
                        <li>Reset</li>  
                    </ol>
                </div>
                
                """,
        unsafe_allow_html=True
    )

        with st.expander("Modulo2"):
           st.markdown(
                """
                <div style='text-align: left;'>
                    <h3>Sentido común 📘</h3>
                    <p>Cuando sacas tu sexto sentido es cuando empieras a ver las cosas diferentes y donde podrás identicar inversiones que el resto no las huelen</p>
                    <ol style="
                        display: inline-block;
                        text-align: left;
                        color: rgb(255,75,75);
                        list-style-position: inside;
                        padding-left: 0;
                    ">
                    <ol>      
                        <li>Toma altura</li>
                        <li>Gafas de niños</li>
                        <li>Empresas ganadoras</li>
                        <li>Horizonte</li>
                        <li>Gestion</li>
                        <li>El tiempo es oro</li>
                    </ol>
                </div>
                
                """,
                unsafe_allow_html=True  
           )    
        with st.expander("Modulo3"):

               st.markdown(
                """
                <div style='text-align: left;'>
                    <h3>Metodo para invertir 📘</h3>
                    <p>Te enseño como lo hacen los ganadores, con un proceso sencillo y seguro pero que solo la disciplina te hára ser un ganador consistente</p>
                    <ol style="
                        display: inline-block;
                        text-align: left;
                        color: rgb(255,75,75);
                        list-style-position: inside;
                        padding-left: 0;
                    ">
                    <ol>      
                        <li>Análisis avanzado de activos y mercados</li>
                        <li>Saber comprar y vender</li>
                        <li>Gestion de capitales</li>
                        <li>Diversificacion de cartera</li>                        
                    </ol>
                </div>
                
                """,
                unsafe_allow_html=True  
           )  
            
        with st.expander("Modulo4"):
            
            st.markdown(
            """
            <div style='text-align: left;'>
                <h3>Inversion Avanzada Cripto 📘</h3>
                <p> Solo vas a invertir en activos tradicionales, hay mas cosas debes conocer te sumerjo en la matrix de inversion avanzada</p>   
                <ol style="
                    display: inline-block;
                    text-align: left;
                    color: rgb(255,75,75);
                    list-style-position: inside;
                    padding-left: 0;
                ">
                <ol>      
                    <li>Blockchain</li>
                    <li>Crypto</li>
                    <li>Bitcoin</li>
                    <li>Ethereum</li>
                    <li>Mineria</li>
                    <li>Custodia y billeteras</li>
                    <li>Lighning</li>
                    <li>Soberania</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True  
        )  
  
                
        with st.expander("Modulo5"):

            st.markdown(
            """
            <div style='text-align: left;'>
                <h3>Inversion Metales 📘</h3>
                <p>Este modulo te va a confirmar , el valor del dinero y de los acivos y como vencer a la inflaccion todos los años en este tipo de inversion historica y segura</p>
                <ol style="
                    display: inline-block;
                    text-align: left;
                    color: rgb(255,75,75);
                    list-style-position: inside;
                    padding-left: 0;
                ">
                <ol>      
                    <li>Historia del dinero</li>
                    <li>Oro</li>
                    <li>Plata</li>
                    <li>Comprar metales</li>
                    <li>Custodia</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True  
        )  
        with st.expander("Modulo6"):
            
            st.markdown(
            """
            <div style='text-align: left;'>
                <h3>Plataforma de inversion 📘</h3>
                <p>Aqui conecamos todos en una aplicacion de inversion que no te dejara solo cuando hagas el curso, será tu herramienta constante para poder gestionar e invertir tus ahorros de forma segura y sencilla</p>
                <ol style="
                    display: inline-block;
                    text-align: left;
                    color: rgb(255,75,75);
                    list-style-position: inside;
                    padding-left: 0;
                ">
                <ol>      
                    <li>Configuracion</li>
                    <li>Selector de activos</li>
                    <li>Gestion de cartera</li>
                    <li>Recursos cryptos</li>
                    <li>Recursos meetales</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True  
        ) 
      
        
if comprar_curso:
    response=requests.post(f"{API_URL}/crear-pago")
    if response.status_code==200:
        st.success(f"Pago enviado:{response.json()}")
        checkout_url = response.json()["url"]
       
        st.markdown(f"[👉 Ir al pago]({checkout_url})", unsafe_allow_html=True)
        #le enviamos un usuario y una contraseña para el acceso login pendiente
    else:
        st.error(f"Error al enviar el pago:{response.text}")
 