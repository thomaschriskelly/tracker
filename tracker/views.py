from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import models
from . import forms

def index(request):
    context = {
        'products': models.Product.objects.all(),
        'product_form': forms.ProductForm(),
    }
    return render(request, 'index.html', context)

def product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            models.Product.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')

def locations(request, product_id):
    if request.method == 'GET':
        product = models.Product.objects.get(id=product_id)
        context = {
            'product': product,
            'breadcrumbs': models.Breadcrumb.objects.filter(product=product),
            'location_form': forms.LocationForm(),
        }
        return render(request, 'locations.html', context)
    elif request.method == 'POST':
        form = forms.LocationForm(request.POST)
        if form.is_valid():
            models.Breadcrumb.objects.create(product=models.Product.objects.get(id=product_id), **form.cleaned_data)
            redirect_url = reverse('locations', args=(product_id,))
            return HttpResponseRedirect(redirect_url)

def location(request, location_id):
    if request.method == 'DELETE':
        to_delete = models.Breadcrumb.objects.get(id=location_id)
        redirect_url = reverse('locations', args=(to_delete.product.id,))
        to_delete.delete()
        return HttpResponse('Success')

def export(request):
    context = {
        'breadcrumbs': models.Breadcrumb.objects.all()
    }
    return render(request, 'export.txt', context)
