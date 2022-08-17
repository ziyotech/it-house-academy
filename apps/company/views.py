from django.shortcuts import render, redirect
from . import models
from .forms import ApplyModelForm

def home(request):
    portfolios = models.Portfolio.objects.all().order_by('id')[:5]
    if request.method == "POST":
        form = ApplyModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = ApplyModelForm()
    return render(request, 'pages/home.html', {"portfolios": portfolios, "form": form})


def dashboard(request):
    contact = models.Contact.objects.all()
    context = {
        "contact": contact
    }
    return render(request, 'pages/dashboard.html', context)

