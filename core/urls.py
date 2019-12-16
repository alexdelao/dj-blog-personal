
from django.urls import path
from .views import AboutTemplateView


urlpatterns = [
    path('about/', AboutTemplateView.as_view(), name='about'),
]

