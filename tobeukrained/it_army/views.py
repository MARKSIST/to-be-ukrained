from django.shortcuts import render


def main(request):
    return render(request, 'it_army/index.html')


def instuctions(request):
    return render(request, 'it_army/instructions.html')


def targets(request):
    return render(request, 'it_army/targets.html')


def results(request):
    return render(request, 'it_army/results.html')
