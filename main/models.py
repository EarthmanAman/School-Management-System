from django.db import models
from django.contrib.auth.models import User



class Grade(models.Model):

	"""
		Descriptios
		-------------
			* A model to store the basic description
			* Can be linked with other database

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
			("three", "GRADE TWO"),
			("four", "GRADE TWO"),
			("five", "GRADE TWO"),
			("six", "GRADE TWO"),
		)

	name		= models.CharField(max_length=10, choices=GRADE_LIST)

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
			* Gender = contains tuple of genders
			*religions = contain tuples of religions

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
	GENDER = (
			("m", "Male"),
			("f", "Female"),
			("o", "Others"),
		)

	RELIGION = (
			("atheists", "Atheists"), ("baha'i", "Baha'i"), ("buddhism", "Buddhism"),
			("christianity", "Christianity"), ("hinduism", "Hinduism"), ("islam", "Islam"),
			("jainism", "Jainism"), ("judaism", "Judaism"), ("shintoism", "Shintoism"),
			("sikhism", "Sikhism"), ("syncretic", "Syncretic"), ("taoism", "Taoism"),
			("tradition", "Tradition"), ("zoroastrianism", "Zoroastrianism"),	

		)

	# Fields 


	nemis_no 	= models.IntegerField(unique=True)

	first_name 	= models.CharField(max_length=100,)
	last_name  	= models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100, null=True)

	dob 		= models.DateField()
	nationality = models.CharField(max_length=100, default="kenya")
	gender 		= models.CharField(max_length=2, choices=GENDER)
	religion 	= models.CharField(max_length=20, choices=RELIGION)


	# Methods 
	def __str__(self):
		return str(self.nemis_no) + " - " + self.first_name + " - " + self.last_name