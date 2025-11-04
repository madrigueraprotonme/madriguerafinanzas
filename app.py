import streamlit as st


home=st.Page("./pages/home.py",title="Mi proyecto",icon="📊")
login=st.Page("./pages/login.py",title="Login",icon="📊")
dasboard=st.Page("./pages/dasboard.py",title="Dasboard",icon="📊")
logout=st.Page("./pages/logout.py",title="Logout",icon="📊")
about=st.Page("./pages/about.py",title="About",icon="📊")
formacion=st.Page("./pages/formacion.py",title="Formacion",icon="📊")
cartera=st.Page("./pages/cartera.py",title="Cartera",icon="📊")
test=st.Page("./pages/test.py",title="Test",icon="📊")
profile=st.Page("./pages/profile.py",title="Profile",icon="📊")
curso=st.Page("./pages/curso.py",title="Curso",icon="📊")
curso_detalle=st.Page("./pages/curso_detalle.py",title="Curso Detalle",icon="📊")
aplicacion=st.Page("./pages/aplicacion.py",title="Aplicacion",icon="📊")
if "logged_in" not in st.session_state:
    st.session_state["logged_in"]=False
  

if st.session_state.logged_in:
    
    pg=st.navigation([profile,cartera,dasboard,logout,formacion,test])

else:
    pg = st.navigation([home,login,about,test,curso,curso_detalle,aplicacion], position="sidebar", expanded=True)
    



pg.run()

