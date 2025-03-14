import xmltodict  #list currency

def name_currency():
    with open("list_currency.xml", "rb") as arquive_currency:  #Open the file in read-only mode and give it a name
        dict_currency = xmltodict.parse(arquive_currency) #create the dictionary (dict_currency) and pass the dictionary (xmltodict)
    
    currency = dict_currency["xml"]
    return currency

#get currency
def disp_converts():
    with open("convert_currency.xml", "rb") as arquive_convert:
        dict_convert = xmltodict.parse(arquive_convert)
    convert = dict_convert["xml"]
    dict_convert_available = {}
    for pair_convert in convert:
        base_currency, targe_currency = pair_convert.split("-")
        if base_currency in dict_convert_available:
            dict_convert_available[base_currency].append(targe_currency)
        else:
            dict_convert_available[base_currency] = [targe_currency]
    return dict_convert_available


