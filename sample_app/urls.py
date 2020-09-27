from django.urls import path
from sample_app.views.root_view import *
from sample_app.views.memo_viewset import *
from rest_framework import routers

urlpatterns = [
    path('', RootView.index, name='index'),
]

router = routers.DefaultRouter()
router.register(r'memo', MemoViewSet)