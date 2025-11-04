import pandas as pd
import streamlit as st
import yfinance as yf
st.session_state["logged_in"]=True
st.title("📊 Dashboard")

tickets=[ "AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "META", "TSLA", "NVDA", "NFLX", "ADBE", "PYPL", "CSCO", "INTC", "AMD", "QCOM", "AVGO", "PEP", "COST", "TXN", "AMGN", "SBUX", "INTU", "GILD", "MDLZ", "BKNG", "ISRG", "VRTX", "ADP", "REGN", "FISV", "LRCX", "MRNA", "KDP", "KLAC", "NXPI", "CSX", "PDD", "PANW", "CRWD", "MELI", "IDXX", "ABNB", "ROST", "MAR", "CTAS", "CHTR", "ODFL", "FTNT", "AZN", "TEAM", "WDAY" ]
años=["1y","2y","3y","4y","5y"]
intervalo=["1mo","1wk"]

with st.container(horizontal=True,border=True,horizontal_alignment="left"):
   
    accion_años=st.selectbox('Visor años',años,width=100)
    accion_intervalo=st.selectbox('Intervalo',intervalo,width=100)


@st.cache_data
def analizar_tickers(tickets,periodo):
    resultados=[]
    
    for t in tickets:
        try:
            data=yf.download(t,period=periodo,progress=False,interval="1mo")
            if data.empty:
                continue
            precios=data["High"]
            maximo=precios.max()
            actual=data["Close"].iloc[-1]
            gap=float(((maximo-actual)/actual)*100)
            
            resultados.append([t,float(maximo),float(actual),round(gap,2)])
        except Exception as e:
            st.warning(f"⚠️ con {t}: {e}")
            continue
    return pd.DataFrame(resultados,columns=["Ticker","Maximo","Actual","Gap"])



col1,col2=st.columns([1,2])
with col1:
    st.header("Screaner")
    screaner = analizar_tickers(tickets, accion_años)
    

    event=st.dataframe(
        screaner,
        key="table",
        on_select="rerun",
        selection_mode="single-cell",
        width="content",
        hide_index=True,
        )



if event.selection.cells:
    fila, columna=event.selection.cells[0]
    accion_seleccionada=screaner.iloc[fila][columna]
    
    data=yf.Ticker(accion_seleccionada)
    df_data=data.history(period=accion_años, interval=accion_intervalo)
    df_grafico=df_data["Close"]
    
    with col2:
        st.header("Grafico")
        st.line_chart(df_grafico,use_container_width=False,width=600)
    
