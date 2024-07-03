from django.urls import path
from . import views

# yaad rkhna ye 'tweet' ke url h, ye url 'localhost:8000/tweet' ke baad ke url ko handle krega
urlpatterns = [
    path("", views.index, name='index' ),
]
