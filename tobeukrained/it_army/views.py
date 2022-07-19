from django.shortcuts import render
from it_army.scripts.exchange_rate import exchangeRatePB

# Create your views here.


def main(request):
    currency = request.GET.get('currency')
    action = request.GET.get('action')
    value = exchangeRatePB(currency, action)
    if action == 'sale':
        text = f'Приват Банк продає валюту {currency} по {value} грн'
    else:
        text = f'Приват Банк купує валюту {currency} по {value} грн'
    #context = {'key_a': key_a}
    context = {'text': text}
    return render(request, 'index.html', context)


def instuctions(request):
    return render(request, 'instructions.html')


def targets(request):
    return render(request, 'targets.html')


def results(request):
    return render(request, 'results.html')
