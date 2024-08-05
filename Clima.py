from os import system
import requests
system("cls")

Siglas = {
    "BR": "Brasil",
    "US": "Estados Unidos",
    "CA": "Canadá",
    "FR": "França",
    "DE": "Alemanha",
    "JP": "Japão",
    "CN": "China",
    "IN": "Índia",
    "RU": "Rússia",
    "ZA": "África do Sul",
    "AR": "Argentina",
    "AU": "Austrália",
    "IT": "Itália",
    "MX": "México",
    "ES": "Espanha",
    "GB": "Reino Unido",
    "KR": "Coreia do Sul",
    "NL": "Países Baixos",
    "TR": "Turquia",
    "SA": "Arábia Saudita",
    "SE": "Suécia",
    "NO": "Noruega",
    "FI": "Finlândia",
    "DK": "Dinamarca",
    "CH": "Suíça",
    "PT": "Portugal",
    "GR": "Grécia",
    "EG": "Egito",
    "NG": "Nigéria",
    "KE": "Quênia",
    "NZ": "Nova Zelândia",
    "SG": "Singapura",
    "MY": "Malásia",
    "ID": "Indonésia",
    "TH": "Tailândia",
    "VN": "Vietnã",
    "PH": "Filipinas",
    "PL": "Polônia",
    "HU": "Hungria",
    "CZ": "República Tcheca",
    "AT": "Áustria",
    "BE": "Bélgica",
    "IE": "Irlanda",
    "IL": "Israel",
    "CL": "Chile",
    "CO": "Colômbia",
    "PE": "Peru",
    "VE": "Venezuela",
    "CU": "Cuba",
    "UA": "Ucrânia",
    "BY": "Bielorrússia",
    "KZ": "Cazaquistão",
    "AE": "Emirados Árabes Unidos",
    "QA": "Catar",
    "KW": "Kuwait",
    "OM": "Omã",
    "PK": "Paquistão",
    "BD": "Bangladesh",
    "LK": "Sri Lanka",
    "MM": "Mianmar",
    "IR": "Irã",
    "IQ": "Iraque",
    "SY": "Síria",
    "LB": "Líbano",
    "JO": "Jordânia",
    "YE": "Iêmen",
    "AF": "Afeganistão",
    "ET": "Etiópia",
    "TZ": "Tanzânia",
    "UG": "Uganda",
    "GH": "Gana",
    "CI": "Costa do Marfim",
    "SN": "Senegal",
    "CM": "Camarões",
    "MG": "Madagáscar",
    "ZM": "Zâmbia",
    "ZW": "Zimbábue",
    "AO": "Angola",
    "MZ": "Moçambique",
    "BW": "Botsuana",
    "NA": "Namíbia",
    "MW": "Malawi",
    "LS": "Lesoto",
    "SZ": "Essuatíni",
    "MR": "Mauritânia",
    "ML": "Mali",
    "BF": "Burquina Fasso",
    "NE": "Níger",
    "TD": "Chade",
    "SD": "Sudão",
    "SS": "Sudão do Sul",
    "LY": "Líbia",
    "TN": "Tunísia",
    "DZ": "Argélia",
    "MA": "Marrocos",
    "EH": "Saara Ocidental",
    "IS": "Islândia",
    "MC": "Mônaco",
    "AD": "Andorra",
    "LI": "Liechtenstein",
    "SM": "San Marino",
    "VA": "Vaticano",
    "LU": "Luxemburgo",
    "MT": "Malta",
    "CY": "Chipre",
    "AM": "Armênia",
    "AZ": "Azerbaijão",
    "GE": "Geórgia",
    "MD": "Moldávia",
    "AL": "Albânia",
    "BA": "Bósnia e Herzegovina",
    "HR": "Croácia",
    "ME": "Montenegro",
    "MK": "Macedônia do Norte",
    "RS": "Sérvia",
    "SI": "Eslovênia",
    "SK": "Eslováquia",
    "BG": "Bulgária",
    "RO": "Romênia",
    "EE": "Estônia",
    "LV": "Letônia",
    "LT": "Lituânia",
    "GL": "Groenlândia",
    "FO": "Ilhas Faroé",
    "GI": "Gibraltar",
    "RE": "Reunião",
    "YT": "Mayotte",
    "MQ": "Martinica",
    "GP": "Guadalupe",
    "GF": "Guiana Francesa",
    "PM": "Saint-Pierre e Miquelon",
    "PF": "Polinésia Francesa",
    "NC": "Nova Caledônia",
    "WF": "Wallis e Futuna",
    "AS": "Samoa Americana",
    "GU": "Guam",
    "MP": "Ilhas Marianas do Norte",
    "PR": "Porto Rico",
    "VI": "Ilhas Virgens Americanas",
    "UM": "Ilhas Menores Distantes dos Estados Unidos",
    "KY": "Ilhas Cayman",
    "BM": "Bermudas",
    "VG": "Ilhas Virgens Britânicas",
    "MS": "Montserrat",
    "TC": "Ilhas Turks e Caicos",
    "AI": "Anguila",
    "SH": "Santa Helena, Ascensão e Tristão da Cunha",
    "FK": "Ilhas Malvinas",
    "GS": "Geórgia do Sul e Ilhas Sandwich do Sul",
    "IO": "Território Britânico do Oceano Índico",
    "VG": "Ilhas Virgens Britânicas",
    "BQ": "Caribe Neerlandês",
    "CW": "Curaçao",
    "SX": "São Martinho",
    "AW": "Aruba",
    "GL": "Groenlândia",
    "IS": "Islândia",
    "JE": "Jersey",
    "GG": "Guernsey",
    "IM": "Ilha de Man",
    "HM": "Ilhas Heard e McDonald",
    "BV": "Ilha Bouvet",
    "TF": "Territórios Franceses do Sul",
    "CK": "Ilhas Cook",
    "NU": "Niue",
    "TK": "Tokelau",
    "WF": "Wallis e Futuna",
    "NF": "Ilha Norfolk",
    "CX": "Ilha Christmas",
    "CC": "Ilhas Cocos (Keeling)",
    "HM": "Ilhas Heard e McDonald",
    "BL": "São Bartolomeu",
    "MF": "São Martinho (parte francesa)",
    "PM": "Saint-Pierre e Miquelon",
    "TF": "Territórios Franceses do Sul",
    "PN": "Pitcairn",
    "TK": "Tokelau",
    "UM": "Ilhas Menores Distantes dos Estados Unidos",
    "SJ": "Svalbard e Jan Mayen",
    "BV": "Ilha Bouvet",
    "IO": "Território Britânico do Oceano Índico",
    "PN": "Ilhas Pitcairn",
    "TK": "Tokelau",
    "TC": "Ilhas Turks e Caicos",
}

def Get(Cidade, API_Key) -> object:
    Base_Url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        'q'     : Cidade,
        'appid' : API_Key,
        'units' : "metric",
        'lang'  : "pt"
    }

    response = requests.get(Base_Url,params=parametros)

    if response.status_code == 200 :
        date = response.json()
        
        Info = {
            'Cidade_Ou_Estado' : date['name'],
            "Pais"             : date['sys']["country"],
            'Temperatura'      : date['main']['temp'],
            'SencTermica'      : date['main']['feels_like'],
            'Umidade'          : date['main']['humidity'],
            'Nuvens'           : date['clouds']['all'],
            'Descricao'        : date['weather'][0]['description'],
        }
        return Info
    else:
        return None


api_key = 'd884f5eec65f3fdbda8169e4129d56c8'

print("\n\033[36m -> Digite o nome de uma cidade ou país para saber a sua atual situação climática <-\033[m\n")

OK = True
while OK:
    Cidade = input("\033[32mCidade ou Estado: \033[33m")
    info = Get(Cidade, api_key)

    if info is not None:
        print(
            f"\033[36m+{'-'*56}\033[m"
            f"\n\033[34m|\033[33m -> \033[34mCidade ou Estado    \033[33m: \033[33m{info['Cidade_Ou_Estado']}    \033[m"
            f"\n\033[34m|\033[33m -> \033[34mPaís                \033[33m: \033[33m{Siglas[info['Pais']]}        \033[m"
            f"\n\033[34m|\033[33m -> \033[34mTemperatura         \033[33m: \033[33m{info['Temperatura']}°C       \033[m"
            f"\n\033[34m|\033[33m -> \033[34mSensação Térmica    \033[33m: \033[33m{info['SencTermica']}°C       \033[m"
            f"\n\033[34m|\033[33m -> \033[34mUmidade             \033[33m: \033[33m{info['Umidade']}%            \033[m"
            f"\n\033[34m|\033[33m -> \033[34mCobertura de Nuvens \033[33m: \033[33mcéu {info['Nuvens']}% Coberto \033[m"
            f"\n\033[34m|\033[33m -> \033[34mDescrição           \033[33m: \033[33m{info['Descricao']}           \033[m"
            f"\n\033[36m+{'-'*56}\033[m"
        )
    else:
        print(
            "\n\033[31mAlgo deu errado! Possíveis erros:\033[m"
            f'\n\033[31m=> Possivelmente \033[33m"{Cidade}"\033[31m não é uma cidade válida'
            f"\n\033[31m=> O servidor pode estar fora do ar\033[m"
            f"\n\033[31m=> Você pode não estar conectado à internet\033[m"
        )
    
    Reset = input("\033[32mContinuar [S/N]: \033[m").strip().upper()
    if Reset == "N":
        break
    while Reset not in ["N", "S"]:
        system("cls")
        print(
            "\n\033[32m[ S ]\033[36m Para Recomeçar \033[m"
            "\n\033[31m[ N ]\033[36m Para Finalizar \033[m"
        )
        Reset = input("\033[32mContinuar [S/N]: \033[m").strip().upper()
        if Reset == "N":
            OK = False
            break

print("\033[m\n")