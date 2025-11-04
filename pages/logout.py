import streamlit as st
st.header("Loouppt")
valor1=st.button("Logout")
st.write(valor1)
if valor1==True:
    st.session_state.clear()
    st.rerun()
    #st.session_state["logged_in"]=False
    #st.session_state["Usuario"]=""
    