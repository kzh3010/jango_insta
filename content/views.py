from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # 피드에 있는 모든 데이터를 가지고 오겠다.

        return render(request, "jinstargram/main.html",context=dict(feeds=feed_list))
