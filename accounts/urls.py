from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . views import UserDetail, UserCreate, UserList

app_name = "accounts"

urlpatterns = [
   path("users.json", UserList.as_view(), name="users"),
   path("users/<str:username>", UserDetail.as_view(), name="user_detail"),
   path("register", UserCreate.as_view()	, name="register"),
   path("login", obtain_auth_token	, name="login"),
] 
