from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = [
        {
            "title": prop.title,
            "description": prop.description,
            "price": str(prop.price),
            "location": prop.location,
            "created_at": prop.created_at,
        }
        for prop in properties
    ]
    return JsonResponse(data, safe=False)

