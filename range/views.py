from django.shortcuts import render
from range.models import price_range

def showobj(request):
    displayvalues = price_range.objects.all()
    return render(request, 'range/home.html', {"range":displayvalues})

def displayvalue(request, id):
    displayprice = price_range.objects.get(id=id)
    context = {'displayprice':displayprice}
    return render(request, 'range/price_range.html', context)
