
from django.urls import path

from content.views import UploadFeed


urlpatterns = [

#     views의 UploadFeed가 url과 매핑이 되야 한다. main.html에 보낸 url과
    path('upload/', UploadFeed.as_view())
]

