import streamlit as st



with st.container():
    col1,col2,col3=st.columns([1,3,1])
    with col2:
        st.markdown(
            """ 
            <div style="text-align: center;">
                <h1>MADRIGUERA APP</h1>
                <h2>Bienvenido a nuestro programa de formacion </h2>
                <p>Aprenderás a invertir en bolsa, junto al colectivo de inversores, utilizando 
                nuestra sistema, que te permitirá invertir en bolsa de forma sencilla y segura.
                no esperes mas si quieres que tus ahorros no se devaluen con el paso del tiempo
                conoce los secretos y alcanlza la libertad                
                </p>
                
            </div>
            """,
            unsafe_allow_html=True, 

        )
        st.image("cabecera.jpg",width="stretch")
        cola,colb,colc=st.columns([4,4,1])
        with colb:
            ver_curso=st.button("Ver curso",type="primary")
