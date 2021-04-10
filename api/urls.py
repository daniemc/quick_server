from django.urls import path
from .views import current_user, UserList, Measures
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('create-user', UserList.as_view()),
    path('user', current_user),
    path('login', obtain_jwt_token),
    path('measures', Measures.as_view()),
]