from rest_framework import serializers
from twitter.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, allow_blank=False)
    tweet = serializers.CharField(max_length=50, allow_blank=False)
    class Meta:
        model = Tweet
        fields = ['name', 'tweet', 'created_date']
