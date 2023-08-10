
from django.urls import path

from .views import Join, Login
#     views에서 정한 class가 url과 매핑이 되야 한다. main.html에 보낸 url과
urlpatterns = [
    path('join/', Join.as_view(), name='join'),
    path('login/', Login.as_view(), name='login')
]

