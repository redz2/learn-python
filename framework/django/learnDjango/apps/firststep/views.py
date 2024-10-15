from django.shortcuts import HttpResponse
from django.http.response import JsonResponse

# Create your views here.


def test(request):
    return HttpResponse("first step test")

def home(request, nid):
    return JsonResponse({"nid": nid})
    
def home2(request):
    # query string: GET 和 POST 方法都可以用
    nid = request.GET.get("nid")
    return JsonResponse({"nid": nid})



