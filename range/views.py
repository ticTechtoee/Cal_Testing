from django.shortcuts import render
from range.models import price_range
from range.models import update_price


def showobj(request):
    selected_range = None
    range_price = price_range.objects.all()

    rate1 = update_price.objects.get(name='rate1')
    rate2 = update_price.objects.get(name='rate2')
    rate3 = update_price.objects.get(name='rate3')
    rate4 = update_price.objects.get(name='rate4')

    if request.method == "POST":
        if 'submit_for_Price_range' in request.POST:
            selected_range = request.POST.get("range")
            range_price = range_price.filter(name=selected_range)
    price = price_range.objects.order_by('name').values_list('name', flat=True)
    context = {'ranges': price, 'range_price': range_price, 'selected_range': selected_range, 'rates1': rate1, 'rates2': rate2, 'rates3': rate3, 'rates4': rate4,}
    return render(request, 'range/price_range.html', context)
