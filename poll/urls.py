from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name='hopme'),
path("about/", views.about, name='about'),
# path('<one>/', views.de, name='detail'),
]
