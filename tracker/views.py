from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import models
from . import forms

def index(request):
    ''' the index of this web application '''
    context = {
        'products': models.Product.objects.all(),
        'product_form': forms.ProductForm(),
    }
    return render(request, 'index.html', context)

def product(request):
    ''' provides the ability to create a new Product resource '''
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            models.Product.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')

def locations(request, product_id):
    '''
    view or create a location resource
    note that what users consider a location is
    a breadcrumb in the database, implying that we
    store more than just a location
    '''
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
    '''
    view to delete a location resource '''
    if request.method == 'DELETE':
        to_delete = models.Breadcrumb.objects.get(id=location_id)
        to_delete.delete()
        return HttpResponse('Success')

def export(request):
    ''' simple view for exporting data '''
    context = {
        'breadcrumbs': models.Breadcrumb.objects.all()
    }
    return render(request, 'export.txt', context)
