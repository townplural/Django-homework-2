from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
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


def sorted_expensive(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all().order_by('-price')
    context = {'phone': phones_all}
    return render(request, template, context)
