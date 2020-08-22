from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.validators import ValidationError

from . permissions import IsOwner
from . serializers import UserSer, UserCreateSer



"""
	APIS
	------
		register ( /register )
		----------------------------
			* Allow registration of user
			
			Allowed Methods
			----------------
				* POST

	

"""

class UserList(ListAPIView):
	serializer_class = UserSer
	queryset = User.objects.all()

class UserDetail(RetrieveUpdateAPIView):
	serializer_class = UserSer
	queryset = User.objects.all()
	permission_classes = [IsAuthenticated, IsOwner]


class UserCreate(CreateAPIView):
	"""
		Description
		-------------
			* A view which allow creation of a user 

		Methods
		---------
			* create(...) - overide the inbuilt create function 
							to enable returning a token to the user

		Improvements
		---------------
			* Access the user instance without fetching it from the db
	"""
	serializer_class = UserCreateSer
	queryset = User.objects.all()
	permission_classes = [AllowAny]

	def create(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		token = None
		data = {}
		message = None
		if serializer.is_valid():

			# Obtain user data
			user_data = serializer.save()
			
			user = User.objects.get(username=user_data["email"])

			# Obtain token
			token = Token.objects.get(user=user).key 

			# Formulating the response
			message = 'Registration successful'
			data["id"] = user.id
			data["email"] = user_data["email"]
			data["first_name"] = user_data["first_name"]
			data["last_name"] = user_data["last_name"]
			
				

		else:
			message = 'Registration unsuccessful'
			data = serializer.errors

		return Response({
            'message': message,
      		"data":data,
            "token": token,
        })