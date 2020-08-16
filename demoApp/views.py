from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    """
        View for the empty path
    :param request: the request from the server
    :return: HttpResponse with basic header
    """
    response = "<h1>Awesome demo app</h1>"
    return HttpResponse(response)


def json(request):
    """
        View for the json/ path
    :param request: the request from the server
    :return: JsonResponse with basic object
    """
    response = {
        "Hello": "World!"
    }
    return JsonResponse(response)


def html(request):
    """
        View for the html/ path
    :param request: the request from the server
    :return: HttpResponse with basic header
    """
    response = "<h4>Hello World!</h4>"
    return HttpResponse(response)
