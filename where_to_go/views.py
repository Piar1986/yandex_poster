from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place, PlaceImage


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


def place_details_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = place.images.all()
    place_images_urls = [place_image.image.url for place_image in place_images]
    place_details = {
        'title': place.title,
        'imgs': place_images_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
            }
        }
    place_details_json = JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    context = {
        'json': place_details_json.content
        }
    return render(request, 'place_details.html', context)