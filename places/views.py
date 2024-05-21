from django.shortcuts import render


def index_page(request):
    context = {
        "title": "Places Remember"
    }
    return render(request, "places/index.html", context=context)
