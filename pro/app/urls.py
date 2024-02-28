from django.urls import path
from . import views
urlpatterns = [
    path('',views.cal,name='cal'),
    # path('',views.cl,name='cl'),
    # path('',views.c,name='c'),
]