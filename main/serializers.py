from django.db import models
from django.contrib.auth.models import User
from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer, 
	SerializerMethodField,
	ListField,
	PrimaryKeyRelatedField,

	ValidationError,

	DateField,
	IntegerField,
	ModelField,
	CharField,
	)

from accounts.serializers import UserSer
from . models import Grade, Pupil, Subject, Teacher

class GradeListSer(ModelSerializer):
	"""
		Description
		-------------
			* A serializer for the grades which will have less but relevant information
			* It will be used when displaying a list of grades
		
		Variables
		-----------
			* No variables

		Methods
		--------
			* No methods
	"""

	
	class Meta:
		model = Grade
		fields = [
			"id",
			"name",
		]


class GradeDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A serializer for the grades which will have detailed information
			* It will be used when displaying a specific grade
		
		Variables
		-----------
			* No variables

		Methods
		--------
			* No methods
	"""

	class Meta:
		model = Grade
		fields = [
			"id",
			"name",
		]


class PupilCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A serializer for the pupils which will have less but relevant information
			* It will be used when displaying a list of pupils
		
		Variables
		-----------
			* No variables
		
		Fields
		-------
			nemis_no
			first_name
			middle_name
			last_name
			dob
			nationality
			gender
			religion


		Methods
		--------
			* No methods
	"""

	class Meta:
		model = Pupil
		fields = [
			"nemis_no",
			"first_name",
			"middle_name",
			"last_name",
			"dob",
			"nationality",
			"gender",
			"religion",
		]


class PupilListSer(ModelSerializer):
	"""
		Description
		-------------
			* A serializer for the pupils which will have less but relevant information
			* It will be used when displaying a list of pupils
		
		Variables
		-----------
			* No variables
		
		Fields
		-------
			nemis_no
			first_name
			middle_name
			last_name
			dob
			nationality
			gender
			religion


		Methods
		--------
			* No methods
	"""
	nemis_no = IntegerField(
		required=True, 
		error_messages={
			"invalid": "Nemis Number must be a number",
			})
	first_name = CharField(
		required=True,
		error_messages={
			"invalid":"First Name should be string",
			"blank": "The field cannot be empty",
		})

	last_name = CharField(
		required=True,
		error_messages={
			"invalid":"Last Name should be string",
			"blank": "The field cannot be empty",
		})

	middle_name = CharField(
		required=False,
		error_messages={
			"invalid":"Middle Name should be string",
			"blank": "The field cannot be empty",
		})

	dob = DateField(
		required=True, 
		error_messages={
			"invalid": "Date should be valid"
			})

	nationality = CharField(
		error_messages={
			"invalid":"Nationality Name should be string",
			"blank": "The field cannot be empty",
		})

	gender = CharField(
		error_messages={
			"invalid":"Gender should be string",
			"blank": "The field cannot be empty",
		})

	religion = CharField(
		error_messages={
			"invalid":"Religion should be string",
			"blank": "The field cannot be empty",
		})

	class Meta:
		model = Pupil
		fields = [
			"nemis_no",
			"first_name",
			"middle_name",
			"last_name",
			"dob",
			"nationality",
			"gender",
			"religion",

			
		]


class PupilDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A serializer for the pupils 
			* It will be used when displaying detail information about a pupil
		
		Variables
		-----------
			* No variables
		
		Fields
		-------
			nemis_no
			first_name
			middle_name
			last_name
			dob
			nationality
			gender
			religion


		Methods
		--------
			* No methods
	"""

	
	school = SerializerMethodField()
	class Meta:
		model = Pupil
		fields = [
			"nemis_no",
			"first_name",
			"middle_name",
			"last_name",
			"dob",
			"nationality",
			"gender",
			"religion",
			"school",
		]

	def get_school(self, obj):
		try:
			school_in = obj.get_school()

			context = {
				"name":school_in.name,
				"school_type":school_in.school_type,
				"county":school_in.county,
				"constitutuency":school_in.constitutuency,
				"ward":school_in.ward,
			}
			return context
		except:
			return None


class SubjectListSer(ModelSerializer):

	"""
		Description
		-------------
			* This is a serializer for the Subject Model
			* It will hold bsic information for the model 
			* Used when displaying all the subjects
		
		Variables
		-----------
			* No variables

		Fields
		--------
			name
			subject_type

		Methods
		---------
	"""

	class Meta:
		model = Subject
		fields = [
			"id",
			"name",
			"subject_type",
			
		]


class SubjectDetailSer(ModelSerializer):

	"""
		
		Descriptions
		--------------
			* A serializer for the Subject Model
			* Will display detailed information about a subject
		
		Variables
		----------
			* No variables

		Fields
		-------
			name
			subject_type

		Methods
		--------	

	"""

	class Meta:
		model = Subject
		fields = [
			"name",
			"subject_type",
		]

class TeacherCreateSer(ModelSerializer):

	"""
		Description
		--------------
			* Serializer for the Teacher Model
			* It will be used for creation purposes

		Variables
		----------
			* user = updating user display

		Fields
		--------
			user
			subjects
			id_no
			employee_id
			phone_no
			dob
	
		Methods
		---------
			* def get_user () = return updated user display

	"""

	# Variables 

	
	# Fields 

	user = PrimaryKeyRelatedField(
		queryset = User.objects.all(),
		error_messages={
			"required": "No user was associated",
			"does_not_exist": "The user you select does not exit",
			"incorrect_type": "The ID of the user was incorrect",
		})


	id_no = IntegerField(
		required=True, 
		error_messages={
			"invalid": "ID Number must be a number",
			})

	employee_id = IntegerField(
		required=True, 
		error_messages={
			"invalid": "Employee Id must be a number",
			})

	phone_no = IntegerField(
		required=True, 
		max_value=10000000000, 
		min_value=0, 
		error_messages={
			"invalid": "Phone Number must be a number", 
			"min_value": "Phone Number cannot be negative",
			"max_value": "Phone Number should not exceed 10 digit",
			})

	class Meta:
		model = Teacher
		fields = [
			"user",
			"subjects",
			"id_no",
			"employee_id",
			"phone_no",
		]


class TeacherListSer(ModelSerializer):

	"""
		Description
		--------------
			* Serializer for the Teacher Model
			* Will handle basic information for teachers
			* Use in displaying list of teachers

		Variables
		----------
			* user = updating user display

		Fields
		--------
			user
			subjects
			id_no
			employee_id
			phone_no
			dob

		Methods
		---------
			* def get_user () = return updated user display

	"""

	# Variables 
	
	subjects = SerializerMethodField()
	user = SerializerMethodField()


	# Fields 

	class Meta:
		model = Teacher
		fields = [
			"user",
			"subjects",
			"id_no",
			"employee_id",
			"phone_no",
			
		]


	# Methods

	def get_subjects(self, obj):
		request = self.context.get("request")
		context = {"request":request}
		return SubjectListSer(obj.subjects, many=True, context=context).data

	def get_user(self, obj):

		return obj.user.first_name + " " + obj.user.last_name


class TeacherDetailSer(ModelSerializer):

	"""
		Descriptions
		-------------
			* Serializer to handle Teacher Model
			* Will handle detailed info about Teacher

		Variables
		----------
			* No variables

		Fields
		-------
			user,
			subjects,
			id_no,
			employee_id,
			phone_no,
			dob,

		Methods
		---------

	"""

	subjects = SerializerMethodField()
	user = SerializerMethodField()

	class Meta:
		model = Teacher
		fields = [
			"user",
			"subjects",
			"id_no",
			"employee_id",
			"phone_no",
		]


	def get_subjects(self, obj):
		
		return SubjectDetailSer(obj.subjects, many=True).data

	def get_user(self, obj):

		return UserSer(obj.user).data
