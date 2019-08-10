from django.http import HttpResponse

def home(request):
    print(request)
    return HttpResponse("<h1>Hello World </h1>")