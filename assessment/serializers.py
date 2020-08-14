from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer, 
	SerializerMethodField,
	StringRelatedField,
	ListField,
	)

from main.serializers import PupilListSer
from institution.serializers import GradeSubjectListSer

from . models import (
	AssessType,
	Assess,
	Result,
	)






class AssessCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* An Assess model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	assess_type
			grade_subject
			date

		Methods
		---------
			* No methods

	"""


	class Meta:
		model = Assess
		fields = [
			"assess_type",
			"grade_subject",
			"date",
		]


class AssessListSer(ModelSerializer):
	"""
		Description
		-------------
			* An Assess model serializer which will be used for few information.

		Variables
		----------
			* assess_tyoe = serialize method field
			*grade_subject = serialize method field


		Fields
		---------
		`	assess_type
			grade_subject
			date

		Methods
		---------
			* No methods

	"""
	
	assess_type = SerializerMethodField()
	grade_subject = SerializerMethodField()

	class Meta:
		model = Assess
		fields = [
			"id",
			"assess_type",
			"grade_subject",
			"date",
		]

	def get_assess_type(self, obj):
		request = self.context.get("request")
		context = {"request":request}
		return AssessTypeListSer(obj.assess_type, context=context).data

	def get_grade_subject(self, obj):
		request = self.context.get("request")
		context = {
			"title": obj.grade_subject.school_subject.subject.name,
			"more": obj.grade_subject.get_indv_url(request)
		}

		return context


class AssessDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* An Assess model serializer which will be used for More information.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	assess_type
			grade_subject
			date

		Methods
		---------
			* No methods

	"""

	assess_type = SerializerMethodField()
	grade_subject = SerializerMethodField()

	class Meta:
		model = Assess
		fields = [
			"assess_type",
			"grade_subject",
			"date",
		]

	def get_assess_type(self, obj):
		return AssessTypeListSer(obj.assess_type).data

	def get_grade_subject(self, obj):
		request = self.context.get("request")
		context = {"request":request}
		return GradeSubjectListSer(obj.grade_subject, context=context).data



class AssessTypeCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* An AssessTypeCreateSer model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	school_grade
			name
			date

		Methods
		---------
			* No methods

	"""


	class Meta:
		model = AssessType
		fields = [
			"school_grade",
			"name",
			"date",
		]


class AssessTypeListSer(ModelSerializer):
	"""
		Description
		-------------
			* An AssessTypeCreateSer model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	school_grade
			name
			date

		Methods
		---------
			* No methods

	"""
	assessments = AssessCreateSer(many=True)

	school_grade = SerializerMethodField()
	class Meta:
		model = AssessType
		fields = [
			"id",
			"school_grade",
			"name",
			"date",

			"assessments"
		]


	def get_school_grade(self, obj):
		request = self.context.get("request")
	
		context = {
			"name": obj.school_grade.grade.name,
			"more": obj.school_grade.get_indv_url(request),
		}

		return context



class AssessTypeDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* An AssessTypeCreateSer model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	school_grade
			name
			date

		Methods
		---------
			* No methods

	"""
	
	school_grade = SerializerMethodField()

	class Meta:
		model = AssessType
		fields = [
			"school_grade",
			"name",
			"date",
			
		]


	def get_school_grade(self, obj):
		request = self.context.get("request")
		context = {
			"title": obj.school_grade.grade.name,
			"more": obj.school_grade.get_indv_url(request),
		}

		return context



class ResultCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* An Result model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	assess
			pupil
			marks
		Methods
		---------
			* No methods

	"""

	def __init__(self, *args, **kwargs):
		many = kwargs.pop('many', True)
		super(ResultCreateSer, self).__init__(many=many, *args, **kwargs)

	class Meta:
		model = Result
		fields = [
			"assess",
			"pupil",
			"marks",
		]



class ResultListSer(ModelSerializer):
	"""
		Description
		-------------
			* An Result model serializer which will be used for few information.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	assess
			pupil
			marks
		Methods
		---------
			* No methods

	"""

	subject = SerializerMethodField()
	assess = SerializerMethodField()
	pupil = SerializerMethodField()

	class Meta:
		model = Result
		fields = [
			"subject",
			"assess",
			"pupil",
			"marks",
		]

	def get_assess(self, obj):
		return obj.assess.assess_type.name

	def get_subject(self, obj):
		return obj.assess.grade_subject.school_subject.subject.name

	def get_pupil(self, obj):

		return obj.pupil.nemis_no


class ResultDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* An Result model serializer which will be used for more information.

		Variables
		----------
			* No Variables

		Fields
		---------
		`	assess
			pupil
			marks
		Methods
		---------
			* No methods

	"""

	assess = SerializerMethodField()
	pupil = SerializerMethodField()

	class Meta:
		model = Result
		fields = [
			"assess",
			"pupil",
			"marks",
		]

	def get_assess(self, obj):
		return AssessListSer(obj.assess).data

	def get_pupil(self, obj):

		return PupilListSer(obj.pupil).data