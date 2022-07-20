from django.shortcuts import render
from tools.scripts.exchange_rate import exchangeRatePB


def index(request):
    currency = request.GET.get('currency')
    action = request.GET.get('action')
    value = exchangeRatePB(currency, action)
    if action == 'sale':
        text = f'Приват Банк продає валюту {currency} по {value} грн'
    else:
        text = f'Приват Банк купує валюту {currency} по {value} грн'
    #context = {'key_a': key_a}
    context = {'text': text}
    return render(request, 'tools/index.html', context)
