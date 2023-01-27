from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, "entry_app/index.html")


def service(request):
    return render(request, "entry_app/service.html")


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid")
            return HttpResponseRedirect("/")
        else:
            return render(request, "entry_app/contact.html", {"form": form})
    else:
        return render(request, "entry_app/contact.html", {"form": form})


def about(request):
    return render(request, "entry_app/about.html")
