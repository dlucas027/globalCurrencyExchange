import requests  
import customtkinter
from get_currency import name_currency, disp_converts
from api import convert_api
#window, size and theme
customtkinter.set_appearance_mode("dark") #general theme
customtkinter.set_default_color_theme("dark-blue") #theme of buttons and icons

window = customtkinter.CTk() #CTK request
window.geometry("500x500") #window size

convert = disp_converts()

#create buttons, texts and other elements
tittle = customtkinter.CTkLabel(window, text="Currency Converter", font=("",20)) #title - font in tuple, first value will be the font type and then the font size
base_currency = customtkinter.CTkLabel(window, text="Select the source currency") #currency selection source
target_currency = customtkinter.CTkLabel(window, text="Choose the currency you want to convert to")#target currency selection

def loading_target_currency(select_currency):
    currency_list = convert[select_currency]
    select_target_currency.configure(values=currency_list)
    select_target_currency.set(currency_list[0])


select_base_currency =customtkinter.CTkOptionMenu(window, values=list(convert.keys()), command=loading_target_currency)#select coins icon
select_target_currency =customtkinter.CTkOptionMenu(window, values=["select your target currency"])

def convert_currency():   
    source_currency = select_base_currency.get()
    destination_currency = select_target_currency.get()
    if source_currency and destination_currency:
        conversion = convert_api(source_currency, destination_currency)
        text_exchange.configure(text=f"1 {source_currency} = {conversion} {destination_currency}")

button_convert = customtkinter.CTkButton(window, text="Convert", command=convert_currency) #convert button

list_currency = customtkinter.CTkScrollableFrame(window)

text_exchange = customtkinter.CTkLabel(window, text="")

available_currencies = name_currency()
for code_currency in available_currencies: #for each currency in the currency list, my text will be the currency variable
    currencies = available_currencies[code_currency]
    text_currencies = customtkinter.CTkLabel(list_currency, text=f"{code_currency}: {currencies}")
    text_currencies.pack()

#colocate all elements on the screen
tittle.pack(padx=10, pady=10)#icones, texts and their distances
base_currency.pack(padx=10, pady=10)
select_base_currency.pack(padx=10)
target_currency.pack(padx=10, pady=10)
select_target_currency.pack(padx=10)
button_convert.pack(padx=10, pady=10)
text_exchange.pack(padx=10, pady=10)
list_currency.pack(padx=10, pady=10)#Use ipadx and ipady to increase the widget's internal space

#this looping keeps the window active
window.mainloop()