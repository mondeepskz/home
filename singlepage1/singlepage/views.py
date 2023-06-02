from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):

    return render (request, 'singlepage/index.html')

    

def section (request, num):

    if 1 <= num <= 3:

        texts = ["1111111","2222222","3333333"]
        return HttpResponse(texts[num - 1])
    
    else:
        raise Http404("No section")
