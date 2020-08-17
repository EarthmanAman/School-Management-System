from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APITestCase

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


class Users(APITestCase):

	def create_un_user(self):
		return User.objects.create(username="un user", password="password")

	def create_user(self, is_superuser=False, is_staff=False):
		user = User.objects.create(
				username="testcase@gmail.com",
				email= "testcase@gmail.com",
				first_name= "test",
				last_name= "test",
				password= "password",
				is_staff= is_staff,
				is_superuser=is_superuser,
			)
		
		return user

	def create_subject(self):
		subject = Subject.objects.create(
				name="test subject",
				subject_type="su",
			)

		return subject

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

	def create_unschool_teacher(self):
		user = User.objects.create(username="unschoolteacher@gmail.com", password="password")
		teacher = Teacher.objects.create(
					user=user,
					id_no= 1245373,
					employee_id= 2234222,
					phone_no= 3462709,
					dob= "1984-08-08",
					)
		return teacher


