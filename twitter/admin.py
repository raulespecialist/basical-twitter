from django.contrib import admin
from twitter.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet, TweetAdmin)
