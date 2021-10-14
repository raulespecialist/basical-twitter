from rest_framework import routers
from django.urls import path, include
from twitter import views

router = routers.DefaultRouter()
router.register(r'twitter', views.TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
