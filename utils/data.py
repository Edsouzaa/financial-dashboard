# Importa a biblioteca yfinance que é referenciada no codigo por yf
import yfinance as yf
# O que é yfinance? é uma biblioteca que permite buscar dados hístoricos de mercado,
# sem precisar utilizar chaves de API.

# Importa o módulo os para manipulação de arquivos e pastas
import os

# ticker nesse caso é utilizado para busca do historico de determinada bolsa.
def get_stock(ticker):
    
    # Seta o ticker como um objeto, contendo suas informações
    ticker_obj = yf.Ticker(ticker)
    
    # Define o historico da ação baseado no period, neste caso 5 anos(5 years)
    data = ticker_obj.history(period="5y")
    
    # Tratamento de excessão: Caso data esteja VAZIO o codigo devolve um aviso.
    if data.empty:
        print(f"AVISO: nenhum dado retornado para {ticker}")
        return data
    
    # Cria a pasta "data" caso ela não exista
    os.makedirs("data", exist_ok=True)

    # Salva o histórico em um arquivo CSV
    data.to_csv(f"data/{ticker}_historico.csv")

    print(f"Histórico salvo em data/{ticker}_historico.csv")
    
    return data