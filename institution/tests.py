import json
import random

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from assessment.models import AssessType, Assess, Result
from main.models import Grade, Pupil, Subject, Teacher
from . models import (
	School,
	SchoolTeacher,
	SchoolGrade,
	SchoolSubject,
	GradeSubject,
	GradeClass,
	ClassPupil,
	TeacherRole,
	PupilRole,
	 )

class GradeClassTest(APITestCase):

	def create_grade(self):
		grade = Grade.objects.create(name="one")

		return grade
	
class Users(APITestCase):

	def setUp(self):
		self.r_user = self.create_user()
		self.subject = self.create_subject()
		self.subject2 = self.create_subject(name="subject 2")
		self.school = self.create_school()
		self.teacher = self.create_teacher(user=self.r_user)
		self.school_teacher = self.create_school_teacher(school=self.school, teacher=self.teacher, position="ht")
		self.token = self.generate_token(self.r_user)
		self.api_authentication()

		self.grade = self.create_grade()
		self.school_grade = self.create_school_grade()
		self.school_subject = self.create_school_subject()
		self.grade_subject = self.create_grade_subject()
		self.grade_class = self.create_grade_class()
		
		self.pupil = self.create_pupil_users()
		self.class_pupil = self.create_class_pupil()

		self.assess_type = self.create_assess_type()
		self.assess = self.create_assess()
		self.result = self.create_result()

	def generate_token(self, user):
		return Token.objects.get(user=user)

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

	def create_un_user(self, is_superuser=False):
		return User.objects.create(username="un user", password="password", is_superuser=is_superuser)

	def create_user(self, username="testcase@gmail.com", is_superuser=False, is_staff=False):
		user = User.objects.create(
				username=username,
				email= "testcase@gmail.com",
				first_name= "test",
				last_name= "test",
				password= "password",
				is_staff= is_staff,
				is_superuser=is_superuser,
			)
		
		return user

	
	def create_teacher(self, user, subject=[]):
		teacher = Teacher.objects.create(
				user= user,
				id_no= 1234567,
				employee_id=222222,
				phone_no= 345627,
				dob="1984-08-08",
			)

		teacher.subjects.set(subject)
		teacher.save()
		return teacher

	def create_school(self):
		school = School.objects.create(
				name="test school",
				school_type= "pu",
				county= "test county",
				constitutuency= "test const",
				ward= "test ward",
			)

		return school

	def create_school_teacher(self, school, teacher, position="s"):
		school_teacher = SchoolTeacher.objects.create(
				school= school,
				teacher= teacher,
				employment_status= "p",
				position=position,
			)

		return school_teacher

	def create_unschool_teacher(self, username="unschoolteacher@gmail.com"):
		user = User.objects.create(username=username, password="password")
		teacher = Teacher.objects.create(
					user=user,
					id_no= 1245373,
					employee_id= 2234222,
					phone_no= 3462709,
					dob= "1984-08-08",
					)
		return teacher

	def create_grade(self):

		return Grade.objects.create(name="one")

	def create_school_grade(self):

		return SchoolGrade.objects.create(grade=self.grade, school=self.school)

	def create_subject(self, name="test sub"):
		return Subject.objects.create(name=name, subject_type="su")

	def create_school_subject(self):

		return SchoolSubject.objects.create(subject=self.subject, school=self.school)

	def create_grade_subject(self):
		grade_subject = GradeSubject.objects.create(
				school_grade = self.school_grade,
				school_subject = self.school_subject,
				subject_teacher = self.school_teacher,
			)

		return grade_subject

	def create_grade_class(self):
		grade_class = GradeClass.objects.create(
				name="east",
				school_grade= self.school_grade,
				class_teacher= self.school_teacher,
			)

		return grade_class
	def create_pupil_users(self):
		pupil = Pupil.objects.create(
				nemis_no=random.randint(20, 100),
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		return pupil

	def create_class_pupil(self):

		class_pupil = ClassPupil.objects.create(
				grade_class= self.grade_class,
				pupil=self.pupil
			)

	def create_assess_type(self):
		assess_type = AssessType.objects.create(
				school_grade= self.school_grade,
				name= "assessment",
				date= "2020-09-24",
			)

		return assess_type
	def create_assess(self):
		assess = Assess.objects.create(
				assess_type = self.assess_type,
				grade_subject = self.grade_subject,
				date= "2020-09-23"
			)
		return assess

	def create_result(self):
		result = Result.objects.create(
				assess= self.assess,
				pupil = self.pupil,
				marks= "80",
			)

		return result
# CREATE

class SchoolCreateTestCase(Users):

	schools = reverse("institution:schools")

	def test_authenticated_head_create(self):

		response = self.client.post(
			
				self.schools,
				{
					"name": "schoo test update",
					"school_type": "pu",
					"county": "kilifi",
					"constitutuency": "kilifi north",
					"ward": "tezo",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_head_create(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.schools,
				{
					"name": "schoo test update",
					"school_type": "pu",
					"county": "kilifi",
					"constitutuency": "kilifi north",
					"ward": "tezo",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SchoolGradeCreate(Users, GradeClassTest):

	school_grades = reverse("institution:school_grades_create")

	def test_authenticated_head_create(self):

		response = self.client.post(
			
				self.school_grades,
				{
					"grade": self.create_grade().id,
					"school": self.school.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_authenticated_unhead_create(self):
		teacher = self.create_unschool_teacher()
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.school_grades,
				{
					"grade": self.create_grade().id,
					"school": self.school.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_authenticated_superuser_create(self):
		
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.school_grades,
				{
					"grade": self.create_grade().id,
					"school": self.school.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SchoolTeacherCreate(Users):

	school_teachers = reverse("institution:school_teachers_create")

	def test_authenticated_head_create(self):
		teacher = self.create_unschool_teacher(username="school teacher create")
		response = self.client.post(
			
				self.school_teachers,
				{
					"school": self.school.id,
					"teacher": teacher.id,
					"employment_status": "p",
					"position": "ht",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.school_teachers,
				{
					"school": self.school.id,
					"teacher": teacher.id,
					"employment_status": "p",
					"position": "ht",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	

	def test_authenticated_unhead_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.school_teachers,
				{
					"school": self.school.id,
					"teacher": teacher.id,
					"employment_status": "p",
					"position": "ht",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_authenticated_superuser_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.school_teachers,
				{
					"school": self.school.id,
					"teacher": teacher.id,
					"employment_status": "p",
					"position": "ht",
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class SchoolSubjectCreate(Users):

	school_subjects_create = reverse("institution:school_subjects_create")

	def test_authenticated_head_create(self):
		response = self.client.post(
			
				self.school_subjects_create,
				{
					"school": self.school.id,
					"subject": self.subject.id
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_create(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.school_subjects_create,
				{
					"school": self.school.id,
					"subject": self.create_subject(name="subject create").id
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	
	def test_authenticated_unhead_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.school_subjects_create,
				{
					"school": self.school.id,
					"subject": self.create_subject(name="subject create").id
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_superuser_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.school_subjects_create,
				{
					"school": self.school.id,
					"subject": self.create_subject(name="subject create").id
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class GradeSubjectCreate(Users):

	grade_subjects_create = reverse("institution:grade_subjects_create")

	def test_authenticated_head_create(self):
		response = self.client.post(
			
				self.grade_subjects_create,
				{
					"school_grade": self.school_grade.id,
					"school_subject": self.school_subject.id,
					"subject_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_create(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.grade_subjects_create,
				{
					"school_grade": self.school_grade.id,
					"school_subject": self.school_subject.id,
					"subject_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	
	def test_authenticated_unhead_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.grade_subjects_create,
				{
					"school_grade": self.school_grade.id,
					"school_subject": self.school_subject.id,
					"subject_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_superuser_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.grade_subjects_create,
				{
					"school_grade": self.school_grade.id,
					"school_subject": self.school_subject.id,
					"subject_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)




class GradeClassTestCreate(Users):

	grade_classes_create = reverse("institution:grade_classes_create")

	def test_authenticated_head_create(self):
		response = self.client.post(
			
				self.grade_classes_create,
				{
					"name": "west",
					"school_grade": self.school_grade.id,
					"class_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_create(self):
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.grade_classes_create,
				{
					"name": "west",
					"school_grade": self.school_grade.id,
					"class_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	
	def test_authenticated_unhead_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.grade_classes_create,
				{
					"name": "west",
					"school_grade": self.school_grade.id,
					"class_teacher": self.school_teacher.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_superuser_create(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.grade_classes_create,
				{
					"name": "west",
					"school_grade": self.school_grade.id,
					"class_teacher": self.school_teacher.id,
				
				},
				format="json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class GradeClassPupilTestCreate(Users):

	class_pupils_create = reverse("institution:class_pupils_create")
	
	def test_authenticated_head_create(self):
		pupil = Pupil.objects.create(
				nemis_no=849339,
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)

		response = self.client.post(
			
				self.class_pupils_create,
				{
					"grade_class": self.grade_class.id,
					"pupil": pupil.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_unauthenticated_create(self):
		pupil = Pupil.objects.create(
				nemis_no=849339,
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		self.client.force_authenticate(user=None)
		response = self.client.post(
			
				self.class_pupils_create,
				{
					"grade_class": self.grade_class.id,
					"pupil": pupil.id,
				
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	
	def test_authenticated_un_classteacher_create(self):
		pupil = Pupil.objects.create(
				nemis_no=849339,
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		teacher = self.create_unschool_teacher(username="unclass teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.class_pupils_create,
				{
					"grade_class": self.grade_class.id,
					"pupil": pupil.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_authenticated_classteacher_create(self):
		pupil = Pupil.objects.create(
				nemis_no=849339,
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		teacher = self.create_unschool_teacher(username="unhead class_teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		gradeClass = self.grade_class
		gradeClass.class_teacher = school_teacher
		gradeClass.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)

		response = self.client.post(
			
				self.class_pupils_create,
				{
					"grade_class": self.grade_class.id,
					"pupil": pupil.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_superuser_create(self):
		pupil = Pupil.objects.create(
				nemis_no=849339,
				first_name="testhd pupil",
				last_name= "testsj pupil",
				middle_name= "test middle",
				nationality= "kenya",
				dob= "2015-01-23",
				gender= "f",
				religion= "christianity",
			)
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.post(
			
				self.class_pupils_create,
				{
					"grade_class": self.grade_class.id,
					"pupil": pupil.id,
				
				},
				format="json"
			)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)





# List 
class SchoolListTestCase(Users):

	list_url = reverse("institution:schools")

	def test_authenticated_schools(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schools(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class SchoolGradeListTestCase(Users):

	list_url = reverse("institution:school_grades")

	def test_authenticated_schools(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schools(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class SchoolTeacherListTestCase(Users):

	list_url = reverse("institution:school_teachers")

	def test_authenticated_schoolteacher(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schoolteacher(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class SchoolSubjectListTestCase(Users):

	list_url = reverse("institution:school_subjects")

	def test_authenticated_schoolsubject(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schoolteacher(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class GradeSubjectListTestCase(Users):

	list_url = reverse("institution:grade_subjects")

	def test_authenticated_schoolsubject(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schoolteacher(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class GradeClasstListTestCase(Users):

	list_url = reverse("institution:grade_classes")

	def test_authenticated_schoolsubject(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated_schoolteacher(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ClassPupilListTestCase(Users):

	list_url = reverse("institution:class_pupils")

	def test_authenticated(self):

		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def test_unauthenticated(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	



# DETAIL

class SchoolDetailTestCase(Users):

	detail = reverse("institution:schools_detail", kwargs={"pk":1})

	
	def test_authenticated_schools_detail(self):

		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_teacher_update(self):

		user = self.create_unschool_teacher()
		self.client.force_authenticate(user=user.user)

		response = self.client.put(
			self.detail, 
			{
				"name": "schoo test update",
				"school_type": "pu",
				"county": "kilifi",
				"constitutuency": "kilifi north",
				"ward": "tezo",
				
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_ht_teacher_update(self):

		response = self.client.put(
			self.detail, 
			{
				"name": "schoo test update",
				"school_type": "pu",
				"county": "kilifi",
				"constitutuency": "kilifi north",
				"ward": "tezo",
				
			})

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher())
		self.client.force_authenticate(user=user.teacher.user)
		
		response = self.client.put(
			self.detail, 
			{
				"name": "schoo test update",
				"school_type": "pu",
				"county": "kilifi",
				"constitutuency": "kilifi north",
				"ward": "tezo",
				
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SchoolGradeDetailTestCase(Users):

	detail = reverse("institution:school_grades_detail", kwargs={"pk":1})

	
	def test_authenticated_schools_detail(self):

		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_teacher_update(self):

		user = self.create_unschool_teacher()
		self.client.force_authenticate(user=user.user)

		response = self.client.put(
			self.detail, 
			{
				"grade": self.grade.id,
				"school": self.school.id,
				
			})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_ht_teacher_update(self):

		response = self.client.put(
			self.detail, 
			{
				"grade": self.grade.id,
				"school": self.school.id,
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher())
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"grade": self.grade.id,
				"school": self.school.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
	
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"grade": self.grade.id,
				"school": self.school.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)



class SchoolTeacherDetailTestCase(Users):

	detail = reverse("institution:school_teachers_detail", kwargs={"pk":1})

	
	def test_authenticated_schools_detail(self):

		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_schools_detail(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_athenticated_teacher_update(self):

		user = self.create_unschool_teacher(username="test test test")
		self.client.force_authenticate(user=user.user)

		response = self.client.put(
			self.detail, 
			{
					"school": self.school.id,
					"teacher": user.id,
					"employment_status": "t",
					"position": "ht",
				
				})

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_ht_schoolteacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"teacher": teacher.id,
				"employment_status": "t",
				"position": "ht",
			
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["employment_status"], "t")

	def test_athenticated_s_teacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher(username="school teacher test"))
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"teacher": teacher.id,
				"employment_status": "p",
				"position": "ht",
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"teacher": teacher.id,
				"employment_status": "t",
				"position": "ht",
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content)["employment_status"], "t")




class SchoolSubjectDetailTestCase(Users):

	detail = reverse("institution:school_subjects_detail", kwargs={"pk":1})

	
	def test_authenticated_detail(self):
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_detail(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_athenticated_teacher_update(self):
		user = self.create_unschool_teacher(username="test test test")
		self.client.force_authenticate(user=user.user)
		
		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"subject": self.subject2.id
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_ht_schoolteacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"subject": self.subject2.id,
			
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):

		teacher = self.create_unschool_teacher(username="unhead")
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher(username="school teacher test"))
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"subject": self.subject2.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
		
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"school": self.school.id,
				"subject": self.subject2.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		


class GradeSubjectDetailTestCase(Users):

	detail = reverse("institution:grade_subjects_detail", kwargs={"pk":1})

	
	def test_authenticated_detail(self):
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_detail(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_athenticated_update(self):
		user = self.create_unschool_teacher(username="test test test")
		self.client.force_authenticate(user=user.user)
		
		response = self.client.put(
			self.detail, 
			{
				"school_grade": self.school_grade.id,
				"school_subject": self.school_subject.id,
				"subject_teacher": self.school_teacher.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_teacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		response = self.client.put(
			self.detail, 
			{
				"school_grade": self.school_grade.id,
				"school_subject": self.school_subject.id,
				"subject_teacher": self.school_teacher.id,
			
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):

		teacher = self.create_unschool_teacher(username="unhead")
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher(username="school teacher test"))
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"school_grade": self.school_grade.id,
				"school_subject": self.school_subject.id,
				"subject_teacher": self.school_teacher.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
		
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"school_grade": self.school_grade.id,
				"school_subject": self.school_subject.id,
				"subject_teacher": self.school_teacher.id,
			
			}
			)


class GradeClassDetailTestCase(Users):

	detail = reverse("institution:grade_classes_detail", kwargs={"pk":1})

	
	def test_authenticated_detail(self):
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_detail(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_athenticated_update(self):
		user = self.create_unschool_teacher(username="test test test")
		self.client.force_authenticate(user=user.user)
		
		response = self.client.put(
			self.detail, 
			{
				"name": "west",
				"school_grade": self.school_grade.id,
				"class_teacher": self.school_teacher.id,
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_teacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead")
		response = self.client.put(
			self.detail, 
			{
				"name": "west",
				"school_grade": self.school_grade.id,
				"class_teacher": self.school_teacher.id,
			
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):

		teacher = self.create_unschool_teacher(username="unhead")
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher(username="school teacher test"))
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"name": "west",
				"school_grade": self.school_grade.id,
				"class_teacher": self.school_teacher.id,
			
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
		
		teacher = self.create_unschool_teacher(username="unhead")
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"name": "west",
				"school_grade": self.school_grade.id,
				"class_teacher": self.school_teacher.id,
			
			}
			)



class ClassPupilDetailTestCase(Users):

	detail = reverse("institution:class_pupils_detail", kwargs={"pk":1})

	
	def test_authenticated_detail(self):
		
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unauthenticated_detail(self):
		self.client.force_authenticate(user=None)
		response = self.client.get(self.detail)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_athenticated_update(self):
		user = self.create_unschool_teacher(username="test test test")
		self.client.force_authenticate(user=user.user)
		
		response = self.client.put(
			self.detail, 
			{
				"grade_class": self.grade_class.id,
				"pupil": self.pupil.id,
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_athenticated_teacher_update(self):
		response = self.client.put(
			self.detail, 
			{
				"grade_class": self.grade_class.id,
				"pupil": self.pupil.id,
			
			}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_classteacher_update(self):
		teacher = self.create_unschool_teacher(username="unhead class_teacher")
		school_teacher = self.create_school_teacher(school=self.school, teacher=teacher)
		gradeClass = self.grade_class
		gradeClass.class_teacher = school_teacher
		gradeClass.save()

		self.client.force_authenticate(user=school_teacher.teacher.user)
		response = self.client.put(
			
				self.detail,
				{
					"grade_class": self.grade_class.id,
					"pupil": self.pupil.id,
				
				},
				format="json"
			)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_athenticated_s_teacher_update(self):

		teacher = self.create_unschool_teacher(username="unhead")
		user = self.create_school_teacher(school=self.school, teacher=self.create_unschool_teacher(username="school teacher test"))
		self.client.force_authenticate(user=user.teacher.user)

		response = self.client.put(
			self.detail, 
			{
				"grade_class": self.grade_class.id,
				"pupil": self.pupil.id,
			}
			)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


	def test_athenticated_superuser_update(self):
		
		
		self.client.force_authenticate(user=self.create_un_user(is_superuser=True))

		response = self.client.put(
			self.detail, 
			{
				"grade_class": self.grade_class.id,
				"pupil": self.pupil.id,
			}
			)

		self.assertEqual(response.status_code, status.HTTP_200_OK)