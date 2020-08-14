from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from rest_framework.reverse import reverse as api_reverse

from . validators import validate_id_no

class Grade(models.Model):

	"""
		Descriptions
		-------------
			* A model to store the basic description
			* Can be linked with other database

		Variables
		-----------
			* _GRADES = a tuple containing grades

		Fields
		-------
			* name - to store the name of thegrade

		Methods
		--------
			* def __str__() - to define the name which will be used to refer it in admin panel


	"""
	GRADE_LIST 	= (
			("one", "GRADE ONE"),
			("two", "GRADE TWO"),
			("three", "GRADE Three"),
			("four", "GRADE Four"),
			("five", "GRADE Five"),
			("six", "GRADE Six"),
		)

	name		= models.CharField(max_length=10, choices=GRADE_LIST)


	def get_list(self):
		return Grade.objects.all()

	def get_list_url(self, request=None):
		return api_reverse("main:grades", request=request)

	def __str__(self):
		return self.name



class Pupil(models.Model):
	
	"""
		Descriptions
		-------------
			* A model to hold information of pupils 
			*It can be used to expand the database

		Variables
		----------
			* _GENDERS = contains tuple of genders
			* _RELIGIONS = contain tuples of religions

		Fields
		--------
			*nemis_no = A unique field 
			*first_name = character, not empty
			*last_name = character, not empty
			*middle_name = character, can be empty

			*class_grade = a foreign key to ClassGrade
			*dob = date
			*gender = character
			*nationality = character
			*religion = character

		Methods
		---------
			* def __str__() = display

	"""


	# Variables
	_GENDERS = (
			("m", "male"),
			("f", "female"),
			("o", "others"),
		)

	_RELIGIONS = (
			("atheists", "atheists"), ("baha'i", "Baha'i"), ("buddhism", "buddhism"),
			("christianity", "christianity"), ("hinduism", "hinduism"), ("islam", "islam"),
			("jainism", "jainism"), ("judaism", "judaism"), ("shintoism", "shintoism"),
			("sikhism", "sikhism"), ("syncretic", "syncretic"), ("taoism", "taoism"),
			("tradition", "tradition"), ("zoroastrianism", "zoroastrianism"),	

		)

	# Fields 


	nemis_no 	= models.IntegerField(unique=True)

	first_name 	= models.CharField(max_length=100,)
	last_name  	= models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100, null=True)

	dob 		= models.DateField()
	nationality = models.CharField(max_length=100, default="kenya")
	gender 		= models.CharField(max_length=2, choices=_GENDERS)
	religion 	= models.CharField(max_length=20, choices=_RELIGIONS)


	# Methods 

	def get_school(self):
		return self.classpupil.grade_class.school_grade.school

	def __str__(self):
		return str(self.nemis_no) + " - " + self.first_name + " - " + self.last_name


class Subject(models.Model):

	"""
		Description
		-------------
			* A model which stores information about a subject
			* Can be used to expand the database

		Variables
		----------
			* _SUBJECTS = a tuple containing type of subjects

		Fields
		--------
			* name = Characters
			* subject_type = Character
		
		Methods
		---------
			* def __str__() = display

	"""

	_SUBJECT_TYPES = (
			("ex", "Extracurriculum"),
			("su", "Subject"),
		)

	name 	= models.CharField(max_length=50)
	subject_type = models.CharField(max_length=2, choices=_SUBJECT_TYPES)


	def __str__(self):
		return self.name


class Teacher(models.Model):

	"""
		
		Descriptions
		--------------
			* A model which extends the django user model
			* Handle Teachers informations

		Variables
		-----------
			* _EMPLOYERS =  a tuple which hold the employer status either Government or private

		Fields
		--------
			* user = foreign key to User model
			* id_no = interger
			* employee_id = integer (can be non for non government)
			* phone_no = integer (must, unique)
			* dob = date

		Methods
		---------
			* def __str__() = display

	"""


	# Variables

	_EMPLOYERS  = (
			("tsc", "TSC"),
			("pr", "Private"),
		)


	# Fields

	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	subjects 	= models.ManyToManyField(Subject, blank=True)
	id_no 		= models.IntegerField(validators=[validate_id_no])
	employee_id = models.IntegerField(blank=True, null=True)
	phone_no 	= models.IntegerField()

	dob 		= models.DateField()


	# Methods

	def validate_id_no(value):
		if type(value) != int:
			raise ValidationError("ID number must be a number")

	def __str__(self):
		return self.user.first_name + " - " + self.user.last_name