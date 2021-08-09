from django.shortcuts import render
from range.models import price_range


# def showobj(request):
#    displayvalues = price_range.objects.all()
#    return render(request, 'range/home.html', {"range":displayvalues})

# def displayvalue(request, id):
#    displayprice = price_range.objects.get(id=id)
#    context = {'displayprice':displayprice}
#    return render(request, 'range/price_range.html', context)

def showobj(request):
    selected_range = None
    range_price = price_range.objects.all()

    if request.method == "POST":
        # Filter restaurants by selected region, but only on a POST
        selected_range = request.POST.get("range")
        range_price = range_price.filter(name=selected_range)

    # Get a list of all unique regions (group by region)
    price = price_range.objects.order_by('name').values_list('name', flat=True)

    context = {
        'ranges': price,
        'range_price': range_price,
        'selected_range': selected_range,
    }

    return render(request, 'range/price_range.html', context)
