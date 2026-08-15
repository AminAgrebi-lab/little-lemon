from django.shortcuts import render

# Create your views here.


def index(request):
    # Render the index.html template as the HTTP response
    return render(request, 'index.html', {})
