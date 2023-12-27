from django.urls import path
from .views import generate_cover_letter

urlpatterns = [
    path('generate-cover-letter/', generate_cover_letter, name='generate_cover_letter'),
]
