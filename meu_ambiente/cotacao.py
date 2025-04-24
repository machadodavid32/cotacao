import requests
from tkinter import Tk, Label, Entry, Button, StringVar

# Função para obter a cotação do dólar
def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    cotacao_dolar = float(dados['USDBRL']['bid'])
    return cotacao_dolar

# Função de conversão
def converter():
    try:
        valor_reais = float(entrada_valor.get())
        cotacao = obter_cotacao_dolar()
        valor_dolar = valor_reais / cotacao
        resultado.set(f"R$ {valor_reais:.2f} = ${valor_dolar:.2f}")
    except ValueError:
        resultado.set("Insira um valor válido.")

# Interface gráfica
janela = Tk()
janela.title("Cotação do Dólar")

# Componentes da interface
Label(janela, text="Valor em Reais:").grid(row=0, column=0, padx=10, pady=10)
entrada_valor = Entry(janela)
entrada_valor.grid(row=0, column=1, padx=10, pady=10)

Button(janela, text="Converter", command=converter).grid(row=1, column=0, columnspan=2, pady=10)

resultado = StringVar()
Label(janela, textvariable=resultado, font=("Arial", 12)).grid(row=2, column=0, columnspan=2, pady=10)

# Executa a interface
janela.mainloop()
