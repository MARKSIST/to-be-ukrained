from this import d
from django.shortcuts import render
from tools.scripts.exchange_rate import exchangeRatePB
from tools.scripts.fuelCostCalculator import fuelCostCalculator
from tools.scripts.fuelCost import fuelCost


def index(request):
    return render(request, 'tools/index.html')


def currency(request):
    currency = request.GET.get('currency')
    action = request.GET.get('action')
    value = exchangeRatePB(currency, action)
    if action == 'sale':
        text = f'Приват Банк продає валюту {currency} по {value} грн'
    else:
        text = f'Приват Банк купує валюту {currency} по {value} грн'
    context = {'text': text}
    return render(request, 'tools/currency.html', context)


def fuel(request):
    cost1Liter = request.GET.get('cost1Liter')
    if cost1Liter is None:
        cost1Liter = 0
    fuelConsumption = request.GET.get('fuelConsumption')
    if fuelConsumption is None:
        fuelConsumption = 0
    distance = request.GET.get('distance')
    if distance is None:
        distance = 0
    result = fuelCostCalculator(
        int(cost1Liter), int(fuelConsumption), int(distance))
    info = fuelCost()
    context = {'totalFuel': result[0],
               'totalPrice': result[1], 'fuelInfo': info}
    return render(request, 'tools/fuel.html', context)
