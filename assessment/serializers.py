from django.db.models import Avg

from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer, 
	Serializer,
	SerializerMethodField,
	StringRelatedField,
	ListField,

	ValidationError,
	)

from main.models import Pupil

from main.serializers import PupilListSer
from institution.serializers import GradeSubjectListSer

from institution.models import SchoolTeacher, GradeSubject, SchoolGrade, ClassPupil
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

	def create(self, validated_data):
		grade_subject = validated_data['grade_subject']
		request = self.context.get("request")

		try:
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			for school_teacher in school_teachers:
				if school_teacher == grade_subject.subject_teacher:
					return validated_data
				elif school_teacher in grade_subject.school_grade.class_teachers():
					return validated_data
				elif heads.exists():
					for head in heads:
						if head.school == grade_subject.school_grade.school:
							return validated_data
			if request.user.is_superuser:
				return validated_data

			raise ValidationError("You do not have permission to do this action")
		except:
			if request.user.is_superuser:
				return validated_data

			raise ValidationError("You do not have permission to do this action")


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

	def create(self, validated_data):
		school_grade = validated_data['school_grade']
		request = self.context.get("request")

		try:

			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)

			heads = school_teachers.filter(position="ht")
			
			for school_teacher in school_teachers:
				if school_teacher in school_grade.class_teachers():
					return validated_data

			if heads.exists():
				for head in heads:
					if head.school == school_grade.school:
						return validated_data

			if request.user.is_superuser:

				return validated_data


			raise ValidationError("You do not have permission to do this action")
		except:
			
			if request.user.is_superuser:
				
				return validated_data

			raise ValidationError("You do not have permission to do this action")

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
	
	def validate(self, validated_data):
		assess = validated_data["assess"]
		pupil = validated_data["pupil"]
		try:
			results = assess.result_set.filter(pupil=pupil)

			return validated_data
		except:
			raise ValidationError("You can create two results for a single student. Please go for update or delete")

	def create(self, validated_data):
		assess = validated_data['assess']
		grade_subject = assess.grade_subject
		request = self.context.get("request")

		try:
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			for school_teacher in school_teachers:
				if school_teacher == grade_subject.subject_teacher:
					return validated_data
				elif school_teacher in grade_subject.school_grade.class_teachers():
					return validated_data
				elif heads.exists():
					for head in heads:
						if head.school == grade_subject.school_grade.school:
							return validated_data
			if request.user.is_superuser:
				return validated_data

			raise ValidationError("You do not have permission to do this action")
		except:
			if request.user.is_superuser:
				return validated_data

			raise ValidationError("You do not have permission to do this action")



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




class ShortResultSer(ModelSerializer):

	name = SerializerMethodField()
	nemis_no = SerializerMethodField()
	class Meta:
		model = Result
		fields = [
			"nemis_no",
			"name",
			"marks",
		]

	def get_name(self, obj):
		return obj.pupil.first_name
	def get_nemis_no(self, obj):
		return obj.pupil.nemis_no


class SubjectAssessDetailSer(ModelSerializer):
	
	
	results = SerializerMethodField()

	class Meta:
		model = Assess
		fields = [
			"id",
			"results",
		]

	
	def get_results(self, obj):
		request = self.context.get("request")
		
		pupils = obj.result_set.all()

		return ShortResultSer(pupils, many=True).data



class AssessTypePupilListSer(ModelSerializer):
	results = SerializerMethodField()
	class Meta:
		model = AssessType
		fields = [
			"id",
			"name",
			"date",
			"results",

		]


	def get_results(self, obj):
		request = self.context.get("request")
		pupil_nemis_no = self.context.get("pupil_nemis_no")
		assesss = Assess.objects.filter(assess_type=obj)
		if assesss.exists():
			assesses = []
			for assess in assesss:
				try:
					pupil_result = assess.result_set.get(pupil__nemis_no=pupil_nemis_no)
					assess_context = { "name": assess.grade_subject.school_subject.subject.name, "marks":pupil_result.marks}
				except:
					assess_context = {}

				assesses.append(assess_context)

			return assesses
		else:
			return []


class AssessPupilListSer(ModelSerializer):

	exam = SerializerMethodField()
	class Meta:
		model = Result
		fields = [
			"exam",
			"marks"
		]

	def get_exam(self, obj):

		return obj.assess.assess_type.name



class AssessTypeMinSer(ModelSerializer):

	subjects = SerializerMethodField()
	class Meta:
		model = AssessType
		fields = [
			"id",
			"name",
			"subjects",
		]

	def get_subjects(self, obj):
		subjects = obj.assessments.all()
		subjects_context = []
		for subject in subjects:
			average = subject.result_set.aggregate(Avg("marks"))
			result_context = {"name":subject.grade_subject.school_subject.subject.name, "average":average["marks__avg"]}

			subjects_context.append(result_context)

		return subjects_context

class AssessPupilsMinSer(ModelSerializer):

	pupils = SerializerMethodField()
	class Meta:
		model = AssessType
		fields = [
			"id",
			"name",
			"pupils",
		]

	def get_pupils(self, obj):

		school_grade_id = self.context.get("school_grade_id")
		grade_pupils = ClassPupil.objects.filter(grade_class__school_grade__id=school_grade_id)
		pupils_context = []
		for grade_pupil in grade_pupils:
			pupil_context = {
				"nemis_no":grade_pupil.pupil.nemis_no, 
				"name":grade_pupil.pupil.first_name,
				"subjects":[]
				}
			results = grade_pupil.pupil.result_set.filter(assess__assess_type=obj)
			for result in results:
				pupil_context["subjects"].append({"name":result.assess.grade_subject.school_subject.subject.name, "marks":result.marks})

			pupils_context.append(pupil_context)

		return pupils_context


def result_avg(results):
	
	if results.count() > 0:
		total = 0
		for result in results:
			total += result.marks
		return total / results.count(), total
	return 0, 0


class AssessMinSer(ModelSerializer):

	exams = SerializerMethodField()
	name = SerializerMethodField()
	class Meta:
		model = Assess
		fields = [
			"id",
			"name",
			"exams",
		]

	def get_name(self, obj):
		return obj.grade_subject.school_subject.subject.name

	def get_exams(self, obj):
		school_grade_id = self.context.get("school_grade_id")
		school_grade = SchoolGrade.objects.get(id=school_grade_id)
		results = obj.result_set.all()
		exams_context_context = []
		for assess_type in school_grade.assesstype_set.all():
			assess_type_results = results.filter(assess__assess_type=assess_type)
			average, total = result_avg(assess_type_results)

			assess_type_context = {"name": assess_type.name, "total":total, "average":average}
			exams_context_context.append(assess_type_context)
		return exams_context_context

		

