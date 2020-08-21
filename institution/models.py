from django.db import models
from main.models import Grade, Pupil, Subject, Teacher

from rest_framework.reverse import reverse as api_reverse


class School(models.Model):

	"""
		Descriptions
		-------------
			* A model which holds the information of schools

		Variables
		----------
			* _SCHOOL_TYPE =  a tuple containing the type of school (public, private)

		Fields
		-------
			* name = character
			* school_type = character
			* county = character
			* constitutuency = character
			* ward = character

		Methods
		---------
			* def __str__() = display

	"""

	# Variables

	_SCHOOL_TYPE 	= (
						("pu", "Public"),
						("pr", "Private"),
					  )

	# Fields

	name 			= models.CharField(max_length=100)
	school_type 	= models.CharField(max_length=3, choices=_SCHOOL_TYPE, default="pu")

	county 			= models.CharField(max_length=50)
	constitutuency 	= models.CharField(max_length=50)
	ward 			= models.CharField(max_length=50)


	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:schools_detail", kwargs={"pk":self.id},  request=request)

	def get_head(self):
		teachers = self.schoolteacher_set.all()
		
		return [teacher for teacher in teachers if teacher["position"] == "ht"]

	def __str__(self):
		return self.name



class SchoolTeacher(models.Model):

	"""
		Description
		-------------
			* A through model to connect school and teacher

		Variables
		-----------
			* _EMPLOYMENT_STATUS = a nested tuple containing employment status (permanent, temporary)
			* _POSITION = a nested tuple containing the position of a teacher (headteacher, deputy, staff)

		Fields
		--------
			* school = foreign key to School
			* teacher = foreign key to Grade
			* employment_status = character 
			* position = character

		Methods
		--------

	"""

	# Variables

	_EMPLOYMENT_STATUS = (
			("p", "Permanent"),
			("t", "Temporary"),
		)

	_POSITION = (
			("ht", "HeadTeacher"),
			("dt", "Deputy Teacher"),
			("s", "staff"),
		)

	#Fields

	school 	= models.ForeignKey(School, on_delete=models.PROTECT)
	teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

	employment_status 	= models.CharField(max_length=2, choices=_EMPLOYMENT_STATUS)	
	position 			= models.CharField(max_length=3, choices=_POSITION, default="s")

	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:school_teachers_detail", kwargs={"pk":self.id},  request=request)


	def __str__(self):
		return self.teacher.__str__()


class SchoolGrade(models.Model):

	"""
		Descriptions
		-------------
			* A Through model to help many to many relationvto Grade

		Variables
		-----------
			* No variable

		Fields
		--------
			* grade = foreign key to Grade
			* school = foreign key to School

		Methods
		---------

	"""


	# Variables


	# Fields

	grade 	= models.ForeignKey(Grade, on_delete=models.PROTECT)
	school 	= models.ForeignKey(School, on_delete=models.PROTECT)

	# Methods
	
	def get_indv_url(self, request=None):
		return api_reverse("institution:school_grades_detail", kwargs={"pk":self.id},  request=request)

	def class_teachers(self):
		grade_classes = self.gradeclass_set.all()
		teachers = []
		for grade_class in grade_classes:
			teachers.append(grade_class.class_teacher)
		return teachers
		
	def __str__(self):
		return self.school.__str__() + " :- " + self.grade.__str__()


class SchoolSubject(models.Model):

	"""
		Descriptions
		-------------
			* A model to for the school subjects

		Variables
		-----------
			* No variables
	
		Fields
		--------
			* school = a foreign key to School
			* subject = a foreign key to subject

		Methods
		---------
			* def __str__() = display
	"""

	# Variables

	# Fields

	school 	= models.ForeignKey(School, on_delete=models.PROTECT)
	subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:school_subjects_detail", kwargs={"pk":self.id},  request=request)

	def __str__(self):
		return self.subject.__str__() + " :- " + self.school.__str__()




class GradeSubject(models.Model):

	"""
		Descriptions
		-------------
			* A model which record the subject of a grade

		Variables
		-----------

		Fields
		--------
			* school_grade = a foreign key to SchoolGrade
			* school_subject = a foreign key to SchoolSubject
			* subject_teacher = a foreign key to SchoolTeacher

		Methods
		---------
			* def __str__() = display
	"""

	school_grade	= models.ForeignKey(SchoolGrade, on_delete=models.PROTECT)
	school_subject 	= models.ForeignKey(SchoolSubject, on_delete=models.PROTECT)
	subject_teacher	= models.ForeignKey(SchoolTeacher, on_delete=models.SET_NULL, null=True)

	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:grade_subjects_detail", kwargs={"pk":self.id},  request=request)

	def __str__(self):
		return self.school_subject.__str__() + " : " + self.school_grade.__str__()



class GradeClass(models.Model):

	"""
		Descriptions
		--------------
			* A model to store the classes in a grade

		Variables
		-----------
			* No variables

		Fields
		--------
			* school_grade = foreign key to SchoolGrade
			* class_teacher = one to one relationship to teacher
			* name = character (default= "default")

		Methods
		---------
			* def __str__() = display
	"""

	# Variables

	# Fields

	school_grade	= models.ForeignKey(SchoolGrade, on_delete=models.PROTECT)
	class_teacher 	= models.ForeignKey(SchoolTeacher, on_delete=models.SET_NULL, null=True)

	name 			= models.CharField(max_length=50, default="default")

	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:grade_classess_detail", kwargs={"pk":self.id},  request=request)

	def __str__(self):
		return self.name + " - " + self.school_grade.grade.name + " - " + self.school_grade.school.name


class ClassPupil(models.Model):

	"""
		Descriptions
		--------------
			* A model to hold the pupils in a class

		Variables
		-----------
			* No variables

		Fields
		--------
			* grade_class = foreign key to GradeClass
			* pupil = one to one field to pupil

		Methods
		--------
		 	* def __str__() = display
	"""

	# Variables

	# Fields

	grade_class	= models.ForeignKey(GradeClass, on_delete=models.CASCADE)
	pupil 		= models.OneToOneField(Pupil, on_delete=models.PROTECT)

	# Methods

	def get_indv_url(self, request=None):
		return api_reverse("institution:class_pupils_detail", kwargs={"pk":self.id},  request=request)


	def __str__(self):

		return self.pupil.first_name + " - " + self.grade_class.__str__()


class TeacherRole(models.Model):

	"""
		Descriptions
		-------------
			* A model for the role of teachers
			* Some roles will be created automatic (headteacher, deputy_teacher, senior_teacher)

		Variables
		-----------
			* No variables

		Fields
		--------
			* teacher = many to many relationship to SchoolTeacher
			* name = character

		Methods
		---------
			* def __str__() = display
	"""

	teacher = models.ManyToManyField(SchoolTeacher)
	name 	= models.CharField(max_length=50)


class PupilRole(models.Model):

	"""
	
		Descriptions
		-------------
			* A model for the role of pupils
			* Some roles will be created automatic (pupil_chairperson, asst_chairperson)

		Variables
		-----------
			* No variables

		Fields
		--------
			* pupil = many to many relationship to SchoolPupil
			* name = character

		Methods
		---------
			* def __str__() = display

	"""

	pupil = models.ManyToManyField(ClassPupil)
	name 	= models.CharField(max_length=50)