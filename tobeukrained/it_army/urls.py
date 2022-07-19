from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('instructions/', views.instuctions),
    path('targets/', views.targets),
    path('results', views.results),
]
