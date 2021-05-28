from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    title = "Title"
    detail = "Detail"
    subtitle = "Subtitle"
    subtitle_detail = "subtitle detail"
    categories = [
        "category 1",
        "category 2",
        "category 3",
        "category 4",
    ]
    links = [
        "google",
        "twitter"
    ]
    created_at = "12/2021"
    tags = [
        "Tag 1",
        "Tag 2",
        "Tag 3",
    ]
    related_news = [
        "Title 1",
        "Title 2",
        "Title 3",
    ]
    return render(request, "blog-details.html",{
        'title': title,
        'created_at': created_at,
        'detail': detail,
        'subtitle': subtitle,
        'subtitle_detail': subtitle_detail,
        'categories': categories,
        'tags': tags,
        'links': links,
        'related_news': related_news,
    })
