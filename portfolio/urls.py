
from django.urls import path
#from . import views
from .views import PortfolioListView


urlpatterns = [
    #path('', views.portfolio, name='portfolio'),
    path('', PortfolioListView.as_view(), name='portfolio'),
]

