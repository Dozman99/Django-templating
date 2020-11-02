from django.shortcuts import render


def index(request):
    return render(request, 'thelistings/listings.html')


def listing(request):
    return render(request, 'thelistings/listing.html')


def search(request):
    return render(request, 'thelistings/search.html')
