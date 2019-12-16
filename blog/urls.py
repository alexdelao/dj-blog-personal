
from django.urls import path
from . import views
from .views import HomeListView, PostDeatilView, PostCreate, PostUpdate, PostDelete


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('blog/<slug:slug>', PostDeatilView.as_view(), name='post'),
    path('blog/create/', PostCreate.as_view(), name='create'),
    path('blog/update/<slug:slug>', PostUpdate.as_view(), name='update'),
    path('blog/delete/<slug:slug>', PostDelete.as_view(), name='delete'),
    
]

