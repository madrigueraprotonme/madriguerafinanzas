import streamlit as st
st.session_state["logged_in"]=False
st.set_page_config(page_title="Madriguera Finanzas",page_icon="📊",layout="wide",initial_sidebar_state="collapsed")

#cabecera
    
st.image("cabecera4.png",width="stretch")
with st.container():
    col1,col2,col3=st.columns([1,3,1])
    with col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <br>
                <h1 style="color:rgb(255,75,75)">MADRIGUERA DE FINANZAS</h1>
                <h1>¿Preparado para dar un gran salto?</h1>
                <h2>Descubre esta madriguera de educacion financiera</h2>
                <p>
                Cunando quieres salir de la <span style="color:rgb(255,75,75)">matrix</span> y no sabes 
                como hacerlo, nosotros te ayudaremos mostrandante los caminos, todos hemso necesitado un guia.</p>
                <p>Estamos en un momento critico, los gobiernos de todos los paises solo saben hacer dos cosas
                <span style="color:rgb(255,75,75)">controlar</span> al ciudadano y <span style="color:rgb(255,75,75)">gastar</span>, imprimiendo dinero de la nada, devaluando la moneda y empobreciendonos
                dia tras dia, devaluando la moneda, y engañando a los trabajadores de bien.
                </p>
                               
               
                
            </div>
            """,
            unsafe_allow_html=True,
        )
        
st.write("")
st.write("")
st.divider()

#bloque de preguntas
with st.container():
    col1,col2,col3=st.columns([1,3,1])
        
    with col2:
    
        col1,col2=st.columns(2,gap="large")

        with col1:
            
            st.markdown(
                """
                <div style="border-right: 2px solid #bbb; height: 300px; margin-left:20px;background-color: black; color: white; padding: 40px 20px; border-radius: 12px;">
                    <h1 style="text-align:center">¿Es importante aprender a invertir?</h1>
                    <h1 style="text-align:center; color:rgb(255,75,75)">SI</h1>
                </div>
                
                """,
                
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                """
                <div style="text-align:center;display:flex;flex-direction:column;justify-content: center; align-items: center;height:300px">
                    <h3>La respuesta es rotunda, y cuanto antes empieces mejor</h3>
                    <p>Multiplica tus ahorros, no dependas de nadie.</p>
                    <p>Liberta es lo que nos merecemos todos no unos pocos.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )            
with st.container():
    

 

    col1,col2,col3=st.columns([1,3,1])

    
        
    with col2:
    
        col1,col2=st.columns(2,gap="large")

        with col2:
            
            st.markdown(
                """
                <div style="border-right: 2px solid #bbb; height: 300px; margin-left:20px;background-color: black; color: white; padding: 40px 20px; border-radius: 12px;">
                    <h1 style="text-align:center; color:rgb(255,255,255)">SI</h1>
                    <h2 style="text-align:center; color:rgb(255,75,75)">Protegelos a todos</h2>  
                    <p style="text-align:center; color:rgb(255,75,75)">Enseñales a ellos con tu nuevo conocimiento y experiencia</p>
                </div>
                
                """,
                
                unsafe_allow_html=True,
            )
        with col1:
            st.markdown(
                """
                <div style="text-align:center;display:flex;flex-direction:column;justify-content: center; align-items: center;height:300px">
                    <h1>¿Es tu familia tu gran preoucpacion?</h1>
                    
                </div>
                """,
                unsafe_allow_html=True,
            )
                     
st.write("")
st.write("")
st.divider()      
    
    
with st.container():

    

    col1,col2,col3=st.columns([1,3,1],gap="large")
    
    with col2:
        st.markdown(
            """
            <div style="text-align:center;display:flex;flex-direction:column;justify-content: center; align-items: center;height:300px">
                <h1>Selecciona una madriguera</h1>
                <h4>Descubre cada seccion de esta web rincon por rincon para prepararte para el futuro  </h4>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1,col2,col3,col4=st.columns([1,1,1,1],gap="large")
        with col1:
            st.markdown(
                """
                <div style="text-align:center">
                    <h2>Cursos</h2>
                    
                </div>
                
                """,
                unsafe_allow_html=True,
            )
            st.image("metodo.jpeg",width="stretch")
            ver_curso=st.button("Ver madriguera",type="primary",width="stretch",key="1")
           
        with col2:
            st.markdown(
                """
                <div style="text-align:center">
                    <h2>APP</h2>
                    
                </div>
                
                """,
                unsafe_allow_html=True,
            )
            st.image("metodo.jpeg",width="stretch")
            ver_app=st.button("Ver madriguera",type="primary",width="stretch",key="2")
            
        with col3:
            st.markdown(
                """
                <div style="text-align:center;">
                    <h2>Recursos</h2>
                    
                </div>
                
                """,
                unsafe_allow_html=True,
            )
            st.image("metodo.jpeg",width="stretch")
            st.button("Ver madriguera",type="primary",width="stretch",key="3")
    
        with col4:
            st.markdown(
                """
                <div style="text-align:center">
                    <h2>Mentorias</h2>
                    
                </div>
                
                """,
                unsafe_allow_html=True,
            )
            st.image("metodo.jpeg",width="stretch")
            st.button("Ver madriguera",type="primary",width="stretch",key="4")
if ver_curso:
    st.switch_page("pages/curso.py")
    
if ver_app:
    st.switch_page("pages/aplicacion.py")
    