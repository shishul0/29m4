from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    # print(request.GET)
    title = request.GET.get("title")
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {
        "advertisements": advertisements
    }
    return render(request, 'advertisements/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(
        advs_count=Count("advertisement")
    ).order_by("-advs_count")
    
    context = {
        "users": users
    }
    return render(request, 'advertisements/top-sellers.html', context)

@login_required # настрой шаблоны, чтобы убрать 404
def advertisement_post(request : WSGIRequest):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse('main-page')
            )
    else: 
        form = AdvertisementForm()
    context = {
        "form": form
    }
    return render(request, 'advertisements/advertisement-post.html', context)

def adv_detali(request: WSGIRequest, pk):
    adv = Advertisement.objects.get(id=pk)
    context = {
        "adv": adv
    }
    return render(request, "advertisements/advertisement.html", context)