import re
import requests
import json

URL = 'https://belarusbank.by/api/kursExchange'

USD = 'USD'
EUR = 'EUR'
RUB = 'RUB'
BYN = 'GBP'
PLN = 'PLN'


def load_exchange():  # The function of sending a request to the bank server
    return json.loads(requests.get(URL).text)


# The function of obtaining the necessary data from the result of the request
def get_exchange(currency):
    for exc in load_exchange():
        if currency == 'USD':
            return (exc['USD_in'], exc['USD_out'])
        elif currency == 'EUR':
            return (exc['EUR_in'], exc['EUR_out'])
        elif currency == 'RUB':
            return (exc['RUB_in'], exc['RUB_out'])
        elif currency == 'GBP':
            return (exc['GBP_in'], exc['GBP_out'])
        elif currency == 'PLN':
            return (exc['PLN_in'], exc['PLN_out'])
    return False


usd_info = get_exchange(USD)
eur_info = get_exchange(EUR)
rub_info = get_exchange(RUB)
byn_info = get_exchange(BYN)
pln_info = get_exchange(PLN)
