#Janela 500x500
#titulo
#campos de selecionar moedas de origem e destino
#botao de converter
#lista de exibição com as desacriçõers das moedas
import requests
import customtkinter
from get_currency import name_currency, disp_converts
from api import convert_api

#criar e configurar janela
customtkinter.set_appearance_mode("dark") #tema geral
customtkinter.set_default_color_theme("dark-blue") #tema dos botoes e icones

window = customtkinter.CTk() #requisição
window.geometry("500x500") #tamanho da janela

convert = disp_converts()

#criar botoes, textos e outros elementos
tittle = customtkinter.CTkLabel(window, text="Currency Converter", font=("",20)) #titulo  - fonte em tupla, primeiro valor vai ser o tipo de fonte e depois o tamanho da fonte
base_currency = customtkinter.CTkLabel(window, text="Select the source currency") #moeda origem |texto o
target_currency = customtkinter.CTkLabel(window, text="Choose the currency you want to convert to")#moeda destino

def loading_target_currency(select_currency):
    currency_list = convert[select_currency]
    select_target_currency.configure(values=currency_list)
    select_target_currency.set(currency_list[0])


select_base_currency =customtkinter.CTkOptionMenu(window, values=list(convert.keys()), command=loading_target_currency)#icone de selecionar as moedas
select_target_currency =customtkinter.CTkOptionMenu(window, values=["select your base currency"])

def convert_currency():   #define a função que vai ser usada pra ativar o command
    source_currency = select_base_currency.get()
    destination_currency = select_target_currency.get()
    if source_currency and destination_currency:
        conversion = convert_api(source_currency, destination_currency)
        text_exchange.configure(text=f"1 {source_currency} = {conversion} {destination_currency}")

button_convert = customtkinter.CTkButton(window, text="Convert", command=convert_currency) #botão de converter

list_currency = customtkinter.CTkScrollableFrame(window)

text_exchange = customtkinter.CTkLabel(window, text="")

available_currencies = name_currency()
for code_currency in available_currencies: #loop : para cada moeda dentro da lista de moedas, meu texto vai ser a variavel moeda 
    currencies = available_currencies[code_currency]
    text_currencies = customtkinter.CTkLabel(list_currency, text=f"{code_currency}: {currencies}")
    text_currencies.pack()


#colocar todos elementos na tela
tittle.pack(padx=10, pady=10)#titulo

base_currency.pack(padx=10, pady=10)#moeda destino |texto o
select_base_currency.pack(padx=10)#icone de selecionar moeda destino
target_currency.pack(padx=10, pady=10)#icone de selecionar moeda destino
select_target_currency.pack(padx=10)
button_convert.pack(padx=10, pady=10)
text_exchange.pack(padx=10, pady=10)
list_currency.pack(padx=10, pady=10)


#Rodar janela


window.mainloop()