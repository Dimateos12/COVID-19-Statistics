import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "6dee67ab1amshc4a305f303e4c03p12786bjsnd5039907d432",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
data = response.json()

def wypisz(kraj):
    string =''
    for item in data['response']:
        if item['country'] == kraj.title():
            print("Kraj")
            print(item['country'])
            string += (str(item['country'])+":")
            print("Populacja")
            print(item['population'])
            string += ("\nPopulacja : " +str(item['population'] ))

            string += ("\nNowe przypadki : " +str(item['cases']['new']))

            string += ("\nAktywne przypadki : " + str(item['cases']['active']))

            string += ("\nWyzdrowieni  : " + str(item['cases']['recovered']))

    return string
