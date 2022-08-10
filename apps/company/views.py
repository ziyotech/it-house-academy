from django.shortcuts import render
from . import models

def home(request):
    portfolios = models.Portfolio.objects.all().order_by('id')[:5]
    return render(request, 'pages/home.html', {"portfolios": portfolios})
