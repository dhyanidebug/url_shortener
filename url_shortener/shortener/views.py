from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound
import random,string
from .models import urls
# Create your views here.

# mappings ={}
def create_short_url(request):
    long_url = request.GET.get('long_url')
    key = request.GET.get('key')
    if not key:
        key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=6))
    if not long_url:
        return JsonResponse({"Status": "Failed", "Reason": "Long url is mandatory"})
    
    short_url = f"http://127.0.0.1:8000/{key}"
    try:
        urls.objects.create(long_url=long_url , key=key , short_url=short_url)
        # mappings[key] = long_url
        return JsonResponse({
            "Status": "Success",
            "Long url": long_url,
            "key": key,
            "short_url":short_url})
    except Exception as e:
        return JsonResponse({"Status": "Failed", "Reason": "Mongo Issue"})





def redirect(request,key):
    # long_url = mappings[key]
    data_obj = urls.objects.get(key =key )
    data_obj.impression += 1
    data_obj.save()
    return HttpResponseRedirect(data_obj.long_url)
    # except Exception as e:
    #     return HttpResponseNotFound("Short url not found")


def list_document(request):
    # try:
    obj= urls.objects.all()
    data = list(obj.values())
    return JsonResponse({"Data": data})
    # except Exception as e:
        # return JsonResponse({"Status": "Failed", "Reason": "Mongo Issue"})


# http://127.0.0.1:8000/qcvbrt -> 20
# http://127.0.0.1:8000/abcdef -> 30

# http://127.0.0.1:8000/create -> create_short_url() -> http://yourwebsite.com/{key}
# http://127.0.0.1:8000/{key} -> redirect() -> longurl

# path -> func call
# pymongo==3.12.3