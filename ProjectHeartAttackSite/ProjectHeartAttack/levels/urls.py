from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('level/<int:levels_id>', get_level, name='level'),
    path('newlevels/', index, name='newlevels'),
    path('toplevels/', toplevels, name='toplevels')
]

