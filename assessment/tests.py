import json
import random

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from institution.tests import Users
from main.models import Grade, Pupil, Subject, Teacher


# CREATES

class AssessTypeCreate(Users):

	assess_types_create = reverse("assessment:assess_types_create")

	def test_authenticated_head(self):

		response = self.client.post(
				self.assess_types_create,

				{
					"school_grade": self.school_grade.id,
					"name": "mid term one",
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
				self.assess_types_create,

				{
					"school_grade": self.school_grade.id,
					"name": "mid term one",
					"date": "2020-09-23",
				},

				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_authenticated(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.post(
				self.assess_types_create,

				{
					"school_grade": self.school_grade.id,
					"name": "mid term one",
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_school_staff(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.assess_types_create,

				{
					"school_grade": self.school_grade.id,
					"name": "mid term one",
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_classteacher(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.assess_types_create,

				{
					"school_grade": self.school_grade.id,
					"name": "mid term one",
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AssessCreateTest(Users):

	assess_create = reverse("assessment:assess_create")

	def test_authenticated_head(self):

		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},

				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_authenticated(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_school_staff(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_classteacher(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_subjectteacher(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.assess_create,

				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-23",
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ResultCreateTest(Users):

	result_create = reverse("assessment:result_create")

	def test_authenticated_head(self):

		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},

				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_authenticated(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_school_staff(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_classteacher(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_subjectteacher(self):

		teacher = self.create_unschool_teacher(username="assess type teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.post(
				self.result_create,

				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				},
				format = "json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# LISTS


class AssessTypeListTest(Users):

	list_url = reverse("assessment:assess_types")

	def test_authenticated(self):

		self.client.force_authenticate(user= self.create_un_user())
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated(self):

		self.client.force_authenticate(user= None)
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AssessListTest(Users):

	list_url = reverse("assessment:assess")

	def test_authenticated(self):

		self.client.force_authenticate(user= self.create_un_user())
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated(self):

		self.client.force_authenticate(user= None)
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ResultListTest(Users):

	list_url = reverse("assessment:result")

	def test_authenticated(self):

		self.client.force_authenticate(user= self.create_un_user())
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated(self):

		self.client.force_authenticate(user= None)
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# DETAILS

class AssessTypeDetailTest(Users):

	detail = reverse("assessment:assess_types_detail", kwargs={"pk":1})

	def test_authenticated_retrieve(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unauthenticated_retrieve(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_unschool_teacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_authenticated_update(self):

		self.client.force_authenticate(user=self.create_un_user())

		response = self.client.put(
				self.detail,
				{
					"school_grade": self.school_grade.id,
					"name": "changed name",
					"date": "2020-09-28",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unschool_teacher_update(self):

		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)

		response = self.client.put(
				self.detail,
				{
					"school_grade": self.school_grade.id,
					"name": "changed name",
					"date": "2020-09-28",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"school_grade": self.school_grade.id,
					"name": "changed name",
					"date": "2020-09-28",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"school_grade": self.school_grade.id,
					"name": "changed name",
					"date": "2020-09-28",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["name"], "changed name")

	def test_superuser_update(self):

		user = self.create_un_user(is_superuser=True)
		self.client.force_authenticate(user=user)
		response = self.client.put(
				self.detail,
				{
					"school_grade": self.school_grade.id,
					"name": "changed name",
					"date": "2020-09-28",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["name"], "changed name")



class AssessDetailTest(Users):

	detail = reverse("assessment:assess_detail", kwargs={"pk":1})

	def test_authenticated_retrieve(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unauthenticated_retrieve(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_unschool_teacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_subjectteacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_authenticated_update(self):

		self.client.force_authenticate(user=self.create_un_user())

		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unschool_teacher_update(self):

		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["date"], "2020-09-24")


	def test_subjectteacher_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["date"], "2020-09-24")

	def test_superuser_update(self):

		user = self.create_un_user(is_superuser=True)
		self.client.force_authenticate(user=user)
		response = self.client.put(
				self.detail,
				{
					"assess_type": self.assess_type.id,
					"grade_subject": self.grade_subject.id,
					"date": "2020-09-24",
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["date"], "2020-09-24")



class ResultDetailTest(Users):

	detail = reverse("assessment:result_detail", kwargs={"pk":1})

	def test_authenticated_retrieve(self):
		self.client.force_authenticate(user=self.create_un_user())
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unauthenticated_retrieve(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_unschool_teacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_subjectteacher(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.get(
				self.detail,
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_authenticated_update(self):

		self.client.force_authenticate(user=self.create_un_user())

		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 90,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_unschool_teacher_update(self):

		teacher = self.create_unschool_teacher(username="un  school")
		self.client.force_authenticate(user=teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 90,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_school_staff_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 90,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_classteacher_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_class = self.grade_class
		grade_class.class_teacher = school_teacher
		grade_class.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 90,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["marks"], 90)


	def test_subjectteacher_update(self):
		teacher = self.create_unschool_teacher(username="un  school")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		grade_subject = self.grade_subject
		grade_subject.subject_teacher = school_teacher
		grade_subject.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["marks"], 90)

	def test_superuser_update(self):

		user = self.create_un_user(is_superuser=True)
		self.client.force_authenticate(user=user)
		response = self.client.put(
				self.detail,
				{
					"assess": self.assess.id,
					"pupil": self.pupil.id,
					"marks": 70,
				}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["marks"], 90)