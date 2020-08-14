import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from institution.tests import Users

from . models import Grade, Pupil, Subject, Teacher

"""
	* Authenticated users but not Teachers cannot create a pupil
	* Authenticated users and Teacher cannot create a pupil
	* Authenticated users and Teacher and SchoolTeacher can create a pupil
"""

class MainListTestCase(Users):

	grades = reverse("main:grades")
	subjects = reverse("main:subjects")
	pupils = reverse("main:pupils")
	teachers = reverse("main:teachers")
	teachers_create = reverse("main:teachers_create")

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

	def test_users_authenticated_grades(self):

		response = self.client.get(self.grades)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_authenticated_subjects(self):

		response = self.client.get(self.subjects)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_authenticated_pupils(self):

		response = self.client.get(self.pupils)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_authenticated_teachers(self):

		response = self.client.get(self.teachers)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_unauthenticated_grades(self):
		
		self.client.force_authenticate(user=None)
		response = self.client.get(self.grades)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_users_unauthenticated_pupils(self):
		
		self.client.force_authenticate(user=None)
		response = self.client.get(self.pupils)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_users_unauthenticated_subjects(self):
		
		self.client.force_authenticate(user=None)
		response = self.client.get(self.subjects)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_users_unauthenticated_teachers(self):
		
		self.client.force_authenticate(user=None)
		response = self.client.get(self.teachers)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_users_authenticated_teacher_create(self):
		user = User.objects.create(username="test user", password="password")
		response = self.client.post(
			
				self.teachers_create,
				{
					"user": user.id,
					"id_no": 124567,
					"employee_id": 22222,
					"phone_no": 34627,
					"subjects": set([]),
					"dob":"1984-08-08",
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	