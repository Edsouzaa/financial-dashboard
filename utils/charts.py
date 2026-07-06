# Importa a biblioteca plotly, biblioteca essa responsavel por gerar graficos.
import plotly.graph_objects as go

# Importações de funções.
from utils.data import get_stock
from utils.indicators import moving_average

def stock_chart(data):
    
    # Gera o grafico
    fig = go.Figure()
    
    # Gera uma linha no grafico que segue o objeto data em relação a preço.
    fig.add_trace(
        go.Scatter(
            x = data.index,
            y = data["Close"],
            name = "Preço"
        )
    )
    
    # Gera uma linha no grafico que segue o objeto data em relação a preço.
    fig.add_trace(
        go.Scatter(
            x = data.index,
            y = data["MM20"],
            name = "MM20"
        )
    )
    
    # Gera uma linha no grafico que segue o objeto data em relação a preço.
    fig.add_trace(
        go.Scatter(
            x = data.index,
            y =  data["MM50"],
            name = "MM50"
        )
    )
    return fig

# Função para a comparação de acoes.
def stock_comparison(acoes):
    fig = go.Figure()
    
    for acao in acoes:
        data = get_stock(acao)
        data["MM20"] = moving_average(data, 20)
        data["MM50"] = moving_average(data, 50)
        
        fig.add_trace(
            go.Scatter(
                x = data.index,
                y = data["Close"],
                name = f"{acao} - Preço"
            )
        )
    
        fig.add_trace(
            go.Scatter(
                x = data.index,
                y = data["MM20"],
                name = f"{acao} - MM20"
            )
        )
    
        fig.add_trace(
            go.Scatter(
                x = data.index,
                y =  data["MM50"],
                name = f"{acao} - MM50"
            )
        )
        
    return fig
        