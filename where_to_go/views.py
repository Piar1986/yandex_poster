from django.http import HttpResponse
from django.template import loader
from places.models import Place


def format_coordinate(coordinate):
    return str(coordinate).replace(',', '.')


def index(request):
    template = loader.get_template('index.html')
    places=Place.objects.all()
    places_details = []
    for place in places:
        place_longitude_formated = format_coordinate(place.lng)
        place_latitude_formated = format_coordinate(place.lat)
        places_details.append({
            'title': place.title,
            'longitude': place_longitude_formated,
            'latitude': place_latitude_formated,
            'placeId': 'moscow_legends',
            'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json'
            })
    context = {
        'places':places_details
        }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)