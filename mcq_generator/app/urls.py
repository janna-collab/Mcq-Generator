from django.urls import path
from .views import home, generate_mcq_view

urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate_mcq_view, name='generate_mcq_view'),
]

