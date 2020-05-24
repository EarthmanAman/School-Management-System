from django.db import models
from main.models import Grade, Pupil, Subject, Teacher


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
			* name = character (default= "default")

		Methods
		---------
			* def __str__() = display
	"""

	# Variables

	# Fields

	school_grade	= models.ForeignKey(SchoolGrade, on_delete=models.PROTECT)

	name 			= models.CharField(max_length=50, default="default")

	# Methods

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

	def __str__(self):

		return self.pupil.first_name + " - " + self.grade_class.__str__()
