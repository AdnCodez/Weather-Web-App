# Date/urls.py
from django.urls import path
from .views import index
# from .views import get_name


urlpatterns = [
    # path('',HomePageView.as_view(), name="home"),
    path('', index),
    # path('index/', index),
    # path('', get_name),
]
