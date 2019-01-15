# Date/urls.py
from django.urls import path
from .views import index
from .views import indexTwo


urlpatterns = [
    # path('',HomePageView.as_view(), name="home"),
    path('', index),
    path('city/', indexTwo),
]
