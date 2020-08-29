from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_201_CREATED,
	)

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.validators import ValidationError

from . permissions import IsOwner
from . serializers import UserSer, UserCreateSer, UserSerDetail



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
	serializer_class = UserSerDetail
	queryset = User.objects.all()
	permission_classes = [IsAuthenticated, IsOwner]

	lookup_field = "username"

	def get_serializer_context(self, *args, **kwargs):
		return {"username":self.kwargs.get("username")}


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
		status_code = HTTP_400_BAD_REQUEST
		status = "fail"
		if serializer.is_valid():

			# Obtain user data
			user_data = serializer.save()
			
			user = get_object_or_404(User, username=user_data["email"])

			# Obtain token
			token = get_object_or_404(Token, user=user).key 

			status_code = HTTP_201_CREATED
			# Formulating the response
			message = 'Registration successful'
			data["id"] = user.id
			data["email"] = user_data["email"]
			data["first_name"] = user_data["first_name"]
			data["last_name"] = user_data["last_name"]
			status = "success"

			return Response({
				"status": status,
				"status_code": status_code,
	            'message': message,
	      		"data":data,
	            "token": token,
	        })
		else:
			message = 'Registration unsuccessful'
			errors = serializer.errors

			return Response({
				"status": status,
				"status_code": status_code,
	            'message': message,
	      		"errors":errors,
	     
	        })