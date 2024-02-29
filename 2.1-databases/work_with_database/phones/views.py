from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get("sort")
    template = 'catalog.html'
    if sort_type == 'min_price':
        phones_all = Phone.objects.all().order_by('price')
    elif sort_type == 'max_price':
        phones_all = Phone.objects.all().order_by('-price')
    elif sort_type == 'name':
        phones_all = Phone.objects.all().order_by('name')
    else:
        phones_all = Phone.objects.all()
    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)


def sorted_cheap(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all().order_by('price')
    context = {'phone': phones_all}
    return render(request, template, context)

