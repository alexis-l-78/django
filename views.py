from django.http import HttpResponse 


def index(request):
    return HttpResponse("Hello, it's the polls index")
