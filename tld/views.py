# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Domain, Registrar, Cheapest, Price
from .models import Blog, Comment
from .data import PriceData
from django.db.models import Max, Min


def index(request):
    prices = PriceData.get_price()
    return render(request, 'index.html', {'prices': prices})


def reviews(request):
    registrars = Registrar.objects.all()
    return render(request, 'reviews.html', {'registrars': registrars})

# Registrar Review Page
def review(request, name):
    registrar = Registrar.objects.filter(keyword=name)
    if registrar:
        return render(request, 'review.html')
    else:
        return render(request, '404.html')

def tlds(request):
    domains = Domain.objects.order_by("label")

    return render(request, 'tlds.html', {'domains': domains})


def domain(request, name):
    domain_extension = Domain.objects.get(name=name)

    if domain_extension:
        prices = domain_extension.price_set.all()
        allcount = len(prices)
        maxprice = prices.aggregate(Max('promo'))
        minprice = prices.aggregate(Min('promo'))
        content = {'domain': domain_extension, 'prices': prices, 'count': allcount, 'max': maxprice, 'min': minprice}

        return render(request, 'tld_base.html', content)
    else:
        return render(request, '404.html')



#About Page
def about(request):
    title = 'About'
    return render(request, 'about.html', {'title': title})

#Contact Page
def contact(request):
    title = 'Contact'
    return render(request, 'contact.html', {'title': title})


def blogindex(request):
    blogs = Blog.objects.all()
    return render(request, 'blogindex.html', {'blogs': blogs})

def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'detail.html', {'blog': blog})


