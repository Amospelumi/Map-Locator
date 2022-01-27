from django.shortcuts import render
from .models import Search

# i install and import folium a python module to get the map i need
import folium

import geocoder

# Create your views here.
def map(request):
    # Country = request.POST.get("address")
    Country = Search.objects.all().last()
    location = geocoder.osm(Country)
    lat = location.lat
    lng = location.lng
    country = location.country
    
    # creating map object
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country, icon=folium.Icon(color='red',icon_color='white')).add_to(m)

    # get html representation of the map object above
    m = m._repr_html_()

    context = {
        'm':m,
    }
    return render(request, "index.html", context)

