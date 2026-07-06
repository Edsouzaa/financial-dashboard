# o que é Streamlit? Streamlit é uma biblioteca que permite criar de forma fácil aplicativos web.
import streamlit as st

# Importações de funções
from utils.data import get_stock
from utils.indicators import moving_average
from utils.charts import stock_chart
from utils.charts import stock_comparison

# Titulo da Dashboard
st.title("Dashboard Financeiro")

ticker = st.text_input(
    "Ticker", # Titulo da inserção de texto
    "PETR4.SA" # Texto base. Sempre vai ser isso que vai estar escrito quando iniciar.
)

dados = get_stock(ticker)

dados["MM20"] = moving_average(dados, 20)
dados["MM50"] = moving_average(dados, 50)

# Mostra a tabela baseada em dados
st.plotly_chart(stock_chart(dados))

st.metric(
    "Preço Atual",
    round(dados["Close"].iloc[-1], 2)
)

st.metric(
    "Máxima",
    round(dados["High"].max(), 2)
)

st.metric(
    "Mínima",
    round(dados["Low"].min(), 2)
)

acoes = st.multiselect(
    "Ações",
    ["PETR4.SA", "VALE3.SA", "ITUB4.SA"],
    default=["PETR4.SA"]
)

# Dashboard de comparação de acoes
st.plotly_chart(stock_comparison(acoes))


def comparison_metrics(acoes):
    if len(acoes) == 0:
        st.metric("Preços", "Aguardando tickers para comparação.")
        st.metric("Máximas", "Aguardando tickers para comparação.")
        st.metric("Mínimas", "Aguardando tickers para comparação.")
        return
        
    precos = []
    maximas = []
    minimas = []

    for acao in acoes:
        dados = get_stock(acao)
        # Calculo do preço atual.
        preco = round(dados["Close"].iloc[-1], 2)
        precos.append(preco)
        
        maxima = round(dados["High"].max(), 2)
        maximas.append(maxima)
        
        minima = round(dados["Low"].min(), 2)
        minimas.append(minima)
    
    colunas = st.columns(len(acoes))
    
    for i, acao in enumerate(acoes):
        with colunas[i]:
            st.metric(f"{acao} - Preço", precos[i])
            st.metric(f"{acao} - Máxima", maximas[i])
            st.metric(f"{acao} - Mínima", minimas[i])

comparison_metrics(acoes)
    
        
        
        