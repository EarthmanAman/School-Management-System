import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from institution.tests import Users

from . serializers import UserSer

user = Users()
h_user = Users(is_head=True)
s_h_user = Users(is_head=True, is_staff=True)
s_s_h_user = Users(is_head=True, is_staff=True, is_superuser=True)

class RegistrationTestCase(APITestCase):
	data = {
			"email":"test@gmail.com", 
			"confirm_email":"test@gmail.com", 
			"first_name": "Test",
			"last_name": "Test",
			"password":"password",
			}

	def test_registration(self):
		
		response = self.client.post("/accounts/register", self.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)



class UserListTestCase(APITestCase):

	list_url = reverse("accounts:users")
	detail = reverse("accounts:user_detail", kwargs={"pk":1})
	user = Users()
	h_user = Users(is_head=True)
	s_h_user = Users(is_head=True, is_staff=True)
	s_s_h_user = Users(is_head=True, is_staff=True, is_superuser=True)

	def setUp(self):
		self.r_user = user.get_user()

		self.token = Token.objects.get(user=self.r_user)
		self.api_authentication()	

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


	def test_users_list_authenticated(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_list_un_authenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_user_detail_retrieve(self):
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["username"], "testcase@gmail.com")

	def test_user_update(self):
		response = self.client.put(
			self.detail, 
			{
				"username":"testcase@gmail.com",
				"first_name":"test update",
			})

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content), 
				{
					"id":1,
					"username":"testcase@gmail.com",
					"first_name":"test update",
					"last_name":"test",
					"email":"testcase@gmail.com",
				}
			)

	def test_user_update_random(self):
		random_user = User.objects.create(username="random@gmail.com", password="random123")
		self.client.force_authenticate(user=random_user)
		response = self.client.put(
			self.detail, 
			{
				"username":"testcase@gmail.com",
				"first_name":"test update random",
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
	

	def test_user_update_superuser(self):
		random_user = User.objects.create(username="random@gmail.com", password="random123", is_superuser=True)
		self.client.force_authenticate(user=random_user)
		response = self.client.put(
			self.detail, 
			{
				"username":"testcase@gmail.com",
				"first_name":"test update random",
			})

		self.assertEqual(response.status_code, status.HTTP_200_OK)
	