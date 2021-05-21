from django.urls import path
from cms.views import blog, blogDetails


urlpatterns = [
    path('', blog, name="blog"),
    path('blog-details', blogDetails, name="blog-details"),
]
