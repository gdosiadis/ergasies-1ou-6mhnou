from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def calculations(name):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        "symbol": name
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': "9c366c09-96f1-450d-8d35-1acfc6100165",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        parseData = json.dumps(response.json())
        eth0bj = json.loads(parseData)
        y = (eth0bj["data"][name]["quote"]["USD"]["price"])
        return y
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


onkr = []  # ονομα κρυπτονομισματος
poskr = []  # ποσοτητα κρυπτονομισματος
synkr = []  # συνολο κρυπτονομισματος

f = open("ex8.txt", "r")
a = f.read()
grammata = ""
lista = []
f.close()

for b in range(len(a)):
    if (a[b] == " ") or (a[b] == ":") or (a[b] == ",") or (a[b] == "{") or (a[b] == "}") or (a[b] == "\""):
        lista.append(grammata)
        grammata = ""
    else:
        grammata = grammata + a[b]

N = len(lista) - 1
for x in range(N, -1, -1):
    if lista[x] == "":
        lista.pop(x)

N = len(lista) - 1
for i in range(len(lista)):
    if i % 2 == 0:
        name = str(lista[i])
        onkr.append(name)
    else:
        q = lista[i]
        q = int(q)
        poskr.append(q)

for z in range(len(onkr)):
    Sum = calculations(onkr[z])
    synolo = Sum * poskr[z]
    synkr.append(synolo)

for c in range(len(onkr)):
    print("Ta ", onkr[c], "einai ", poskr[c], "kai se dollaria einai: ",
          synkr[c], "$")
