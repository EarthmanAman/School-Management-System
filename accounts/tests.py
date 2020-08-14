import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from institution.tests import Users

from . serializers import UserSer

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



class UserListTestCase(Users):

	
	list_url = reverse("accounts:users")
	detail = reverse("accounts:user_detail", kwargs={"pk":1})

	def setUp(self):
		self.r_user = self.create_user()

		self.token = self.generate_token(self.r_user)
		self.api_authentication()	

	def generate_token(self, user):
		return Token.objects.get(user=user)

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


	def test_users_list_authenticated(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_list_un_authenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	

class UserDetailTestCase(Users):

	detail = reverse("accounts:user_detail", kwargs={"pk":1})

	def setUp(self):
		self.r_user = self.create_user()
		self.subject = self.create_subject()
		self.school = self.create_school()
		self.teacher = self.create_teacher(user=self.r_user)
		self.school_teacher = self.create_school_teacher(school=self.school, teacher=self.teacher)
		self.token = self.generate_token(self.r_user)
		self.api_authentication()	


	def generate_token(self, user):
		return Token.objects.get(user=user)

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

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
	