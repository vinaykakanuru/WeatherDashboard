from app.forms import CityForm
from django.http import HttpResponse
from django.shortcuts import render
from app.utils import get_weather_data
from app.models import City

# Create your views here.


def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data.get('city_name')
            weather_data = get_weather_data(city_name)
    elif request.method == 'GET':
        try:
            city_name = City.objects.latest('date_added').city_name
            weather_data = get_weather_data(city_name)
        except Exception:
            weather_data = None
    return render(request, 'home.html', {'form': form, 'weather_data': weather_data})


def history(request):
    cities = City.objects.all().order_by('-date_added')[:5]

    weather_data_list = []
    for city in cities:
        city_name = city.city_name
        weather_data_list.append(get_weather_data(city_name))

    context = {'weather_data_list': weather_data_list}
    return render(request, 'history.html', context)
