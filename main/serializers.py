from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer, 
	SerializerMethodField,
	ListField,
	)

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