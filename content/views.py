import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Jinstargram.settings import MEDIA_ROOT
from user.models import User
from .models import Feed

class Main(APIView):

    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # 피드에 있는 모든 데이터를 가지고 오겠다.
        print('로그인 한 사용자는 :', request.session['email'])
        email =request.session['email']
        if email is None :
            return render(request, "user/login.html")
        user = User.objects.filter(email=email).first()

        if user is None :
            return render(request, "user/login.html")
        return render(request, "jinstargram/main.html",context=dict(feeds=feed_list, user=user))

class UploadFeed(APIView) :
    def post(self, request):
        #  파일 저장을 위한
        file = request.FILES['file'] # 파일 불러오기
        uuid_name = uuid4().hex # 파일의 고유 아이디 - 관리 편하게 하기 위해 - 랜덤 하이디
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination :
            for chunk in file.chunks():
                destination.write(chunk)
        # 파일 저장을 위한 끝
        image_img = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        # Feed에 저장
        # 가져올 때는 Feed.objects.all() 로 가져왔다면
        # 만들 때는 create()
        Feed.objects.create(image=image_img, content=content, user_id=user_id, profile_image=profile_image, like_count=0)
        return Response(status=200)