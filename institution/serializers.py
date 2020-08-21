from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer, 
	SerializerMethodField,
	ListField,
	ValidationError,
	)

from main.serializers import (
	GradeListSer,
	PupilListSer,
	PupilDetailSer,
	SubjectListSer,
	SubjectDetailSer,
	TeacherListSer, 
	TeacherDetailSer,
	)

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


class SchoolListSer(ModelSerializer):
	"""
		Description
		-------------
			* A school model serializer which will serialize less information about a school

		Variables
		----------
			* No variables

		Methods
		---------
			* No methods

	"""
	class Meta:
		model = School
		fields = [
			"name",
			"school_type",
			"county",
			"constitutuency",
			"ward",
		]


class SchoolDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A school model serializer which will serialize More information about a school

		Variables
		----------
			* No variables

		Methods
		---------
			* No methods

	"""
	class Meta:
		model = School
		fields = [
			"name",
			"school_type",
			"county",
			"constitutuency",
			"ward",
		]


class SchoolTeacherCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolTeacher model serializer which will serialize More information about a school teacher

		Variables
		----------
			* No Variables

		Methods
		---------
			* No methods

	"""


	class Meta:
		model = SchoolTeacher
		fields = [
			"school",
			"teacher",
			"employment_status",
			"position",
		]


class SchoolTeacherListSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolTeacher model serializer which will serialize More information about a school teacher

		Variables
		----------
			* info = serializer methos field it will return a TeacherListSer

		Methods
		---------
			* No methods

	"""
	info = SerializerMethodField()

	class Meta:
		model = SchoolTeacher
		fields = [
			"info",
			"employment_status",
			"position",
		]

	def get_info(self, obj):

		return TeacherListSer(obj.teacher).data



class SchoolTeacherDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolTeacher model serializer which will serialize More information about a school teacher

		Variables
		----------
			* info = serializer methos field it will return a TeacherListSer

		Methods
		---------
			* No methods

	"""
	info = SerializerMethodField()

	class Meta:
		model = SchoolTeacher
		fields = [
			"info",
			"employment_status",
			"position",
		]

	def get_info(self, obj):

		return TeacherDetailSer(obj.teacher).data



class SchoolGradeCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolTeacher model serializer which will serialize More information about a school teacher

		Variables
		----------
			* info = serializer methos field it will return a TeacherListSer

		Methods
		---------
			* No methods

	"""

	class Meta:
		model = SchoolGrade
		fields = [
			"grade",
			"school",
		]



class SchoolGradeListSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolGrade model serializer which will serialize few information about a school teacher

		Variables
		----------
			* info = serializer methos field it will return a TeacherListSer

		Methods
		---------
			* No methods

	"""
	grade = SerializerMethodField()

	class Meta:
		model = SchoolGrade
		fields = [
			"grade",
		]

	def get_grade(self, obj):

		return GradeListSer(obj.grade).data


class SchoolGradeDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolGrade model serializer which will serialize More information about a school teacher

		Variables
		----------
			* grde = serializer methos field it will return a GradeListSer

		Methods
		---------
			* No methods

	"""
	grade = SerializerMethodField()

	class Meta:
		model = SchoolGrade
		fields = [
			"grade",
		]

	def get_grade(self, obj):

		return GradeListSer(obj.grade).data


class SchoolSubjectCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolGrade model serializer which will be used in Creating.

		Variables
		----------
			* No Variables

		Methods
		---------
			* No methods

	"""

	class Meta:
		model = SchoolSubject
		fields = [
			"school",
			"subject",
		]



class SchoolSubjectListSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolSubject model serializer which will serialize Few information about a school subject

		Variables
		----------
			* subjects = serializer methos field it will return a SubjectListSer

		Methods
		---------
			* No methods

	"""
	subjects = SerializerMethodField()

	class Meta:
		model = SchoolSubject
		fields = [
			"subjects",
		]

	def get_subjects(self, obj):

		return SubjectListSer(obj.subject).data


class SchoolSubjectDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A SchoolSubject model serializer which will serialize More information about a school subject

		Variables
		----------
			* subjects = serializer methos field it will return a SubjectListSer

		Methods
		---------
			* No methods

	"""
	subjects = SerializerMethodField()

	class Meta:
		model = SchoolSubject
		fields = [
			"subjects",
		]

	def get_subjects(self, obj):

		return SubjectDetailSer(obj.subject).data



class GradeSubjectCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeSubject model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			school_subject
			subject_teacher

		Methods
		---------
			* No methods

	"""

	class Meta:
		model = GradeSubject
		fields = [
			"school_grade",
			"school_subject",
			"subject_teacher",
		]




class GradeSubjectListSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeSubject model serializer which will contain few information about Grade Subject.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			school_subject
			subject_teacher

		Methods
		---------
			* No methods

	"""

	school_grade = SerializerMethodField()
	school_subject = SerializerMethodField()
	subject_teacher = SerializerMethodField()

	class Meta:
		model = GradeSubject
		fields = [
			"school_grade",
			"school_subject",
			"subject_teacher",
		]

	def get_school_grade(self, obj):

		return SchoolGradeListSer(obj.school_grade).data

	def get_school_subject(self, obj):
		return SchoolSubjectListSer(obj.school_subject).data

	def get_subject_teacher(self, obj):
		return SchoolTeacherListSer(obj.subject_teacher).data



class GradeSubjectDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeSubject model serializer which will contain More information about Grade Subject.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			school_subject
			subject_teacher

		Methods
		---------
			* No methods

	"""

	school_grade = SerializerMethodField()
	school_subject = SerializerMethodField()
	subject_teacher = SerializerMethodField()

	class Meta:
		model = GradeSubject
		fields = [
			"school_grade",
			"school_subject",
			"subject_teacher",
		]

	def get_school_grade(self, obj):

		return SchoolGradeListSer(obj.school_grade).data

	def get_school_subject(self, obj):
		return SchoolSubjectListSer(obj.school_subject).data

	def get_subject_teacher(self, obj):
		return SchoolTeacherListSer(obj.subject_teacher).data




class GradeClassCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A Grade Class Subject model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			class_teacher
			name

		Methods
		---------
			* No methods

	"""

	class Meta:
		model = GradeClass
		fields = [
			"school_grade",
			"class_teacher",
			"name",
		]


class GradeClassListSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeClass model serializer which will contain few information about Grade Class.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			class_teacher
			name

		Methods
		---------
			* No methods

	"""

	school_grade = SerializerMethodField()
	class_teacher = SerializerMethodField()

	class Meta:
		model = GradeClass
		fields = [
			"school_grade",
			"class_teacher",
			"name",
		]

	def get_school_grade(self, obj):
		context = {
			"title": obj.school_grade.grade.name,
			"more":None,
		}
		return context


	def get_class_teacher(self, obj):
		context = {
			"title": f"{obj.class_teacher.teacher.user.first_name} {obj.class_teacher.teacher.user.last_name}",
			"more":None,
		}
		return context
		


class GradeClassDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeClass model serializer which will contain more information about Grade Class.

		Variables
		----------
			* No Variables

		Fields
		--------
			school_grade
			class_teacher
			name

		Methods
		---------
			* No methods

	"""

	school_grade = SerializerMethodField()
	class_teacher = SerializerMethodField()

	class Meta:
		model = GradeClass
		fields = [
			"school_grade",
			"class_teacher",
			"name",
		]

	def get_school_grade(self, obj):
		context = {
			"title": obj.school_grade.grade.name,
			"more":None,
		}
		return context


	def get_class_teacher(self, obj):
		context = {
			"title": f"{obj.class_teacher.teacher.user.first_name} {obj.class_teacher.teacher.user.last_name}",
			"more":None,
		}
		return context
		


class ClassPupilCreateSer(ModelSerializer):
	"""
		Description
		-------------
			* A ClassPupil model serializer which will be used to create.

		Variables
		----------
			* No Variables

		Fields
		--------
			grade_class
			pupil

		Methods
		---------
			* No methods

	"""

	class Meta:
		model = ClassPupil
		fields = [
			"grade_class",
			"pupil",
		]

	def create(self, validated_data):
		grade_class = validated_data['grade_class']
		request = self.context.get("request")

		try:

			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			if grade_class.class_teacher in school_teachers:
				return validated_data

			if heads.exists():
				for head in heads:
					if head.school == grade_class.class_teacher.school:
						return validated_data

			if request.user.is_superuser:

				return validated_data


			raise ValidationError("You do not have permission to do this action")
		except:
			
			if request.user.is_superuser:
				
				return validated_data

			raise ValidationError("You do not have permission to do this action")
	



class ClassPupilListSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradeClass model serializer which will contain few information about Grade Class.

		Variables
		----------
			* No Variables

		Fields
		--------
			grade_class
			pupil

		Methods
		---------
			* No methods

	"""

	grade_class = SerializerMethodField()
	pupil = SerializerMethodField()

	class Meta:
		model = ClassPupil
		fields = [
			"grade_class",
			"pupil",
		]

	def get_grade_class(self, obj):
		context = {
			"title": obj.grade_class.school_grade.grade.name,
			"more":None,
		}
		return context


	def get_pupil(self, obj):
		
		return PupilListSer(obj.pupil).data
		


class ClassPupilDetailSer(ModelSerializer):
	"""
		Description
		-------------
			* A GradePupil model serializer which will contain few information about Grade Pupil.

		Variables
		----------
			* No Variables

		Fields
		--------
			grade_class
			pupil

		Methods
		---------
			* No methods

	"""
	pupil = SerializerMethodField()

	class Meta:
		model = ClassPupil
		fields = [
			"pupil",
		]


	def get_pupil(self, obj):
		
		return PupilDetailSer(obj.pupil).data
		