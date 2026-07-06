# numpy é uma biblioteca voltada para computação científica e análise dados.
import numpy as np
# no caso dessa aplicação em especifico numpy será utilizado para calcular a volatalidade

# Uma função para calculo de media movel.
def moving_average(data, period):
    
    return data["Close"].rolling(period).mean()

# Retono diario é uma métrica financeira que mede a variação percentual do valor de um investimento
# em um periodo de 24horas ou um dia util.
def daily_return(data):

    return data["Close"].pct_change()

# Volatilidade frequencia e intensidade que o preço de um ativo ou variável muda ao longo do tempo.
def volatility(data):

    retorno = daily_return(data)

    return retorno.std() * np.sqrt(252)