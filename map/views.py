from django.shortcuts import render
import folium


# Create your views here.
def map(request):
    # creating map object
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([9.0820, 8.6753]).add_to(m)

    # get html representation of the map object above
    m = m._repr_html_()

    context = {
        'm':m,
    }
    return render(request, "index.html", context)

