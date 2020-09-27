from django.urls import path
from sample_app.views import *

urlpatterns = [
    path('', RootView.index, name='index'),
]