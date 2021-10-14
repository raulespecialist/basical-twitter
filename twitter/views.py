from django.shortcuts import render
from rest_framework import viewsets
from twitter.models import Tweet
from rest_framework import serializers
from twitter.serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

def index(request):
    context = {}
    return render(request, 'twitter/index.html', context)
