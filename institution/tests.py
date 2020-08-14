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
	def __init__(self, is_superuser=False, is_staff=False, registered=True, is_head=False):
		super().__init__()
		self.is_superuser = is_superuser
		self.is_staff = is_staff
		self.registered = registered
		self.is_head = is_head

		self.main()

	def main(self):
		self.user = self.create_user()
		self.subject = self.create_subject()
		self.teacher = self.create_teacher()
		self.school = self.create_school()

		if self.registered:
			self.school_teacher = self.create_school_teacher()

	def create_user(self):
		user = User(
				username="testcase234@gmail.com",
				email= "testcase234@gmail.com",
				first_name= "test",
				last_name= "test",
				password= "password",
				is_superuser = self.is_superuser,
				is_staff= self.is_staff,
			)

		return user

	def create_subject(self):
		subject = Subject.objects.create(
				name="test subject",
				subject_type="su",
			)

		return subject

	def create_teacher(self):
		teacher = Teacher.objects.create(
				user= self.user.id,
				id_no= 1234567,
				employee_id=222222,
				phone_no= 345627,
				dob="1984-08-08",
			)

		teacher.subjects = set([self.subject])
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

	def create_school_teacher(self):
		school_teacher = SchoolTeacher(
				school= self.school,
				teacher= self.teacher,
				employment_status= "p",
			)

		if self.is_head:
			school_teacher["position"] = "ht",
		else:
			school_teacher["position"] = "s"

		school_teacher = school_teacher.save()

		return school_teacher

	def get_user(self):
		return self.user