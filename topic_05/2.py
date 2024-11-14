#2)	Програма конвертування іноземної валюти в українську гривню. 
#Для отримання актуальних курсів валют необхідно використовувати API НБУ та модуль, 
#що надає можливість виконувати запити до сторонніх сервісів requests. Достатня умова роботи – можливість конвертації 
#для трьох іноземних валют EUR, USD, PLN. Користувачу надається можливість 
#введення кількості та типу валюти, результат роботи програми – конвертоване значення в українських гривнях.

import requests

def get_exchange_rate(currency):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    data = response.json()

    for item in data:
        if item['cc'] == currency:
            return item['rate']
    return None

def convert_currency():
    currency = input("Введіть тип валюти (EUR, USD, PLN): ").upper()
    amount = float(input("Введіть кількість: "))

    rate = get_exchange_rate(currency)
    if rate:
        uah = amount * rate
        print(f"{amount} {currency} = {uah:.2f} UAH")
    else:
        print("Невідома валюта або помилка отримання курсу.")

convert_currency()
