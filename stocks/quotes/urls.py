from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about.html', views.about, name = "about"),
    path('portfolio.html', views.portfolio, name = "portfolio"),
    path('delete/<stock_id>', views.delete, name = "delete")
] 