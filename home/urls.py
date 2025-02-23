from django.urls import path
from .views import recommend_crop

urlpatterns = [
    path("", recommend_crop, name="recommend_crop"),
]
