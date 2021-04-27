from django.urls import path
from .views.user import current_user, UserList
from .views.measures import Measures, MeasuresModification
from .views.vendors import Vendors, VendorsModification
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('create-user', UserList.as_view()),
    path('user', current_user),
    path('login', obtain_jwt_token),
    path('measures', Measures.as_view()),
    path('measures/<int:id>', MeasuresModification.as_view()),
    path('vendors', Vendors.as_view()),
    path('vendors/<int:id>', VendorsModification.as_view()),
]
