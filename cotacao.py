import requests

# Função para obter a cotação do dólar
def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"  # URL da API
    resposta = requests.get(url)
    dados = resposta.json()
    cotacao_dolar = float(dados['USDBRL']['bid'])  # Obtém o valor do dólar
    return cotacao_dolar

# Solicita o valor em reais
valor_reais = float(input("Informe o valor em reais que deseja converter para dólares: "))

# Obtém a cotação e faz o cálculo
cotacao = obter_cotacao_dolar()
valor_dolar = valor_reais / cotacao

# Exibe o resultado
print(f"R$ {valor_reais:.2f} equivalem a aproximadamente ${valor_dolar:.2f} dólares com a cotação atual de R$ {cotacao:.2f}.")
