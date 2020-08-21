import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from institution.tests import Users

from . models import Grade, Pupil, Subject, Teacher

"""

"""

	
class PupilClass(APITestCase):

	def create_pupil(self):
		pupil = Pupil.objects.create(
				nemis_no=782829,
				first_name="test pupil",
				last_name= "test pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		
		return pupil


class MainListTestCase(Users):

	grades = reverse("main:grades")
	subjects = reverse("main:subjects")
	pupils = reverse("main:pupils")
	teachers = reverse("main:teachers")
	teachers_create = reverse("main:teachers_create")

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



class MainCreateTestCase(Users):

	grades = reverse("main:grades")
	subjects = reverse("main:subjects")
	pupils = reverse("main:pupils")
	teachers = reverse("main:teachers")
	teachers_create = reverse("main:teachers_create")


	def test_users_authenticated_teacher_create(self):
		user = User.objects.create(username="test user", password="password")
		self.client.force_authenticate(user=user)
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

	def test_users_unauthenticated_teacher_create(self):
		user = User.objects.create(username="test user", password="password")
		self.client.force_authenticate(user=None)
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
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_users_authenticated_pupil_create(self):
		user = User.objects.create(username="test user", password="password")
		self.client.force_authenticate(user=user)
		response = self.client.post(
			
				self.pupils,
				{
					"nemis_no":782829,
					"first_name": "test pupil",
					"last_name": "test pupil",
					"middle_name": "test middle",
					"nationality": "kenya",
					"dob": "2015-01-23",
					"gender": "f",
					"religion": "christianity",
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_users_authenticated_teacher_pupil_create(self):
		user = self.create_unschool_teacher()
		self.client.force_authenticate(user=user.user)
		response = self.client.post(
			
				self.pupils,
				{
					"nemis_no":782829,
					"first_name": "test pupil",
					"last_name": "test pupil",
					"middle_name": "test middle",
					"nationality": "kenya",
					"dob": "2015-01-23",
					"gender": "f",
					"religion": "christianity",
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_users_authenticated_school_teacher_pupil_create(self):
		
		response = self.client.post(
			
				self.pupils,
				{
					"nemis_no":782829,
					"first_name": "test pupil",
					"last_name": "test pupil",
					"middle_name": "test middle",
					"nationality": "kenya",
					"dob": "2015-01-23",
					"gender": "f",
					"religion": "christianity",
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	
class MainPupilDetailTestCase(Users, PupilClass):

	detail = reverse("main:pupils_detail", kwargs={"pk":2})

	
	
	def test_pupil_detail_retrieve(self):
		self.pupil2 = self.create_pupil()
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["first_name"], "test pupil")

	def test_unauthenticated_pupil_detail_retrieve(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_authenticated_pupil_detail_retrieve(self):
		user = User.objects.create(username="test test", password="password")
		self.client.force_authenticate(user=user)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_authenticated_pupil_detail_retrieve(self):
		user = User.objects.create(username="test user", password="password")
		teacher = Teacher.objects.create(
					user=user,
					id_no= 1245373,
					employee_id= 2234222,
					phone_no= 3462709,
					dob= "1984-08-08",
					)
		self.client.force_authenticate(user=user)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_pupil_update(self):
		self.pupil2 = self.create_pupil()
		response = self.client.put(
			self.detail, 
			{
				"nemis_no":782829,
				"first_name":"pupil update",
				"last_name": "test pupil",
				"middle_name": "test middle",
				"nationality": "kenya",
				"dob": "2015-01-23",
				"gender": "f",
				"religion": "christianity",
			})

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content), 
				{
					"nemis_no":782829,
					"first_name": "pupil update",
					"last_name": "test pupil",
					"middle_name": "test middle",
					"nationality": "kenya",
					"dob": "2015-01-23",
					"gender": "f",
					"religion": "christianity",
					"school": None
				}
			)

	def test_unathenticated_pupil_update(self):

		user = self.create_un_user()
		self.client.force_authenticate(user=user)

		response = self.client.put(
			self.detail, 
			{
				"nemis_no":782829,
				"first_name":"pupil update",
				"last_name": "test pupil",
				"middle_name": "test middle",
				"nationality": "kenya",
				"dob": "2015-01-23",
				"gender": "f",
				"religion": "christianity",
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_teacher_pupil_update(self):

		user = self.create_unschool_teacher()
		self.client.force_authenticate(user=user.user)

		response = self.client.put(
			self.detail, 
			{
				"nemis_no":782829,
				"first_name":"pupil update",
				"last_name": "test pupil",
				"middle_name": "test middle",
				"nationality": "kenya",
				"dob": "2015-01-23",
				"gender": "f",
				"religion": "christianity",
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)






class MainTeacherDetailTestCase(Users):

	detail = reverse("main:teachers_detail", kwargs={"pk":1})

	
	def test_detail_retrieve(self):
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_teacher_detail_retrieve(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_authenticated_teacher_detail_retrieve(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_authenticated_teacher_detail_retrieve(self):
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher())
		self.client.force_authenticate(user=user.teacher.user)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	
	def test_athenticated_teacher_update(self):

		user = self.create_unschool_teacher()
		self.client.force_authenticate(user=user.user)

		response = self.client.put(
			self.detail, 
			{
				"user":self.r_user,
				"id_no": 9999,
				"employee_id": 2234222,
				"phone_no": 3462709,
				"dob": "1984-08-08",
				
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_school_staff_teacher_update(self):

		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher())
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"user":self.r_user,
				"id_no": 9999,
				"employee_id": 2234222,
				"phone_no": 3462709,
				"dob": "1984-08-08",
				
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_owner_update(self):

		response = self.client.put(
			self.detail, 
			{
				"user":self.r_user,
				"id_no": 9999,
				"employee_id": 2234222,
				"phone_no": 3462709,
				"dob": "1984-08-08",
				
			})

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
		self.assertEqual(json.loads(response.content)["id_no"], 9999)
