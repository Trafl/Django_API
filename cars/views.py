from django.shortcuts import render
from cars.models import Car


def cars_views(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)

    print(request.GET.get('search'))

    return render(
        request,
        'cars.html',
        {'cars': cars})
