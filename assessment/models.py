from django.db import models

from main.models import Pupil
from institution.models import SchoolGrade, GradeSubject

class AssessManager(models.Manager):

	def assess_types(self, school_grade_id):
		return AssessType.objects.filter(school_grade__id=school_grade_id)

	def assesses(self, school_grade_id):
		return Assess.objects.filter(assess_type__school_grade__id=school_grade_id)

	def subject_assesses(self,assess_type_id, grade_subject_id):
		assesses = Assess.objects.filter(grade_subject__id=grade_subject_id)
		return assesses.filter(assess_type__id=assess_type_id)

	def results(self, assess_id):
		return Result.objects.filter(assess__id=assess_id)
		


class AssessType(models.Model):

	"""
		Description
		------------
			* Amodel for the type of assignment e.g homework, endterm, midterm

		Variables
		----------
			* No variables

		Fields
		--------
			* school_grade = foreign key to SchoolGrade
			* name = character
			* date = date
	"""

	# Variables


	# Fields

	school_grade 	= models.ForeignKey(SchoolGrade, on_delete=models.SET_NULL, null=True)

	name 			= models.CharField(max_length=50)
	date 			= models.DateField()

	objects = AssessManager()
	# Methods

	def __str__(self):
		return self.name + " :- " + self.school_grade.__str__()


class Assess(models.Model):

	"""
		Description
		-------------
			* A model for assessments

		Variables
		-----------
			* No variables

		Fields
		--------
			* assess_type = foreign key to AssessType
			* grade_subject = foreign key to GradeSubject
			* date = date

		Methods
		--------
			* def __str__() = display

	"""

	# Variables

	# Fields

	assess_type		= models.ForeignKey(AssessType, related_name="assessments", on_delete=models.SET_NULL, null=True)
	grade_subject 	= models.ForeignKey(GradeSubject, on_delete=models.SET_NULL, null=True)

	date 			= models.DateField(blank=True, null=True)

	objects = AssessManager()

	# Methods

	def __str__(self):

		return self.grade_subject.__str__() + " :- " + self.assess_type.__str__()


class Result(models.Model):

	"""
		Description
		-------------
			* A model which handle results of assessments

		Variables
		-----------
			* No variable

		Fields
		--------
			* assess = foreign key to Assess
			* pupil = a foreign key to pupil
			* marks = float

		Methods
		--------
			* def __str__() = display
	"""

	# Variable 


	# Fields

	assess 	= models.ForeignKey(Assess, on_delete=models.SET_NULL, null=True)
	pupil 	= models.ForeignKey(Pupil, on_delete=models.CASCADE)

	marks 	= models.FloatField()

	objects = AssessManager()

	# Methods

	def __str__(self):

		return str(self.marks)