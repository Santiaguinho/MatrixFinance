print(" _______  _______ _________ _______ _________")         
print("(       )(  ___  )\__   __/(  ____ )\__   __/|\     /|")
print("| () () || (   ) |   ) (   | (    )|   ) (   ( \   / )")
print("| || || || (___) |   | |   | (____)|   | |    \ (_) / ")
print("| |(_)| ||  ___  |   | |   |     __)   | |     ) _ (  ")
print("| |   | || (   ) |   | |   | (\ (      | |    / ( ) \ ")
print("| )   ( || )   ( |   | |   | ) \ \_____) (___( /   \ )")
print("|/     \||/     \|   )_(   |/   \__/\_______/|/     \|")
print(" ____________________________________by: Pedro Santiago")                      

# -*- coding: utf 8 -*-
import json
import requests
from pprint import pprint


Ação = input("Digite a ação da Empresa: ")

consulta = requests.get('https://api.hgbrasil.com/finance/stock_price?key=fb9ac48d&symbol='+ Ação)

resposta = str(consulta.json()).replace("'", '"').replace(" ", "").lower()
Resultado = json.loads(resposta)

Simbolo =  Resultado["results"][Ação]["symbol"].upper()
print("simbolo da empresa: " + str(Simbolo))

Nome_Da_Empresa=  Resultado["results"][Ação]["name"]
print("nome da empresa: " + str(Nome_Da_Empresa)) 

Preço =  Resultado["results"][Ação]["price"]
print("preço da empresa: " + str(Preço))

Valor_Das_Ações =  Resultado["results"][Ação]["change_percent"]
print("valorização: " + str(Valor_Das_Ações))

Diferença = (Preço * Valor_Das_Ações / 100 * - 1)

Inicial =  (Preço + Diferença)
print ("valor_inical: " + str (Inicial))

print ("/")
print ("/")
print ("/")

if Ação == "bbas3":
  Investimento = 25
  Quantidade = 4

  print ("dinheiro investido: " + str(Investimento * Quantidade))

  lucro = round(((Preço - Investimento)* Quantidade),2)
  print ("lucro atual: "+ str(lucro))
