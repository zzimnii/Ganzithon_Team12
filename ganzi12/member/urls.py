from django.urls import path
from .views import *

app_name = 'member'

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
]