from django.shortcuts import render
from rest_framework.views import APIView
from instapp.models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'main.html',context=dict(feed_list=feed_list))