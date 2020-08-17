from django.shortcuts import render
from django.db import IntegrityError

from rest_framework.generics import (
	GenericAPIView,
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView,
	)

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from institution.models import School
from institution.permissions import IsSchoolTeacher, IsSchoolStaff

from . models import Grade, Pupil, Subject, Teacher
from . permissions import IsSchoolStaffTeacher
from . serializers import (
	GradeListSer, 
	GradeDetailSer,

	PupilCreateSer,
	PupilListSer, 
	PupilDetailSer,

	SubjectListSer,
	SubjectDetailSer,

	TeacherCreateSer,
	TeacherListSer,
	TeacherDetailSer,
)

"""
	APIS
	------
		GradeList ( /grades.json )
		----------------------------
			*Display all the main grades
			
			Allowed Methods
			----------------
				* GET

		GradeDetail (/grades/<int:pk>.json)
		------------------------------------
			* Display detailed info dor a grade

			Allowed Methods
			----------------
				* GET
				* UPDATE
				* DELETE


		PupilList ( /pupils.json )
		----------------------------
			* Display all the pupils
			* Allow creation of a pupil

			Allowed Methods
			----------------
				* GET
				* CREATE


		PupilDetail (/pupils/<int:pk>.json)
		-------------
			* Return detailed information about a pupil, you can update and delete the pupil
			
			Allowed Methods
			----------------
				* GET
				* UPDATE
				* DELETE



		SubjectList (/subjects.json)
		------------------------------
			* Display a list of all Subjects

			Allowed Methods
			----------------
				* GET
				


		SubjectDetail (/subjects/<int:pk>.json)
		----------------------------------------
			* Return detailed info about a specified subject

			Allowed Methods
			----------------
				* GET
				* UPDATE
				* DELETE


		TeacherCreate(/teachers/create.json)
		---------------------------------------
			* Used to create a teacher

			Allowed Methods
			---------------
				* POST

		TeacherList (/teachers.json)
		------------------------------
			* Display a list of all Teachers

			Allowed Methods
			----------------
				* GET
				* CREATE

		TeacherDetail (/teachers/<int:pk>.json)
		----------------------------------------
			* Return detailed info about a specified Teacher
			
			Allowed Methods
			----------------
				* GET
				* UPDATE
				* DELETE

"""

#Grade
# Will not have delete because it is controlled by admin.

class GradeList(ListAPIView):

	serializer_class = GradeListSer
	queryset = Grade.objects.all()


class GradeDetail(RetrieveAPIView):
	serializer_class = GradeDetailSer
	queryset = Grade.objects.all()


# Pupil

class PupilList(ListCreateAPIView):
	"""
		Description
		-------------
			* A view which can list pupils and at the same time you can create a year student.

	"""

	serializer_class = PupilListSer
	queryset = Pupil.objects.all()
	permission_classes = [IsAuthenticated, IsSchoolTeacher]

	def create(self, request, *args, **kwargs):
		try:
			return super(ListCreateAPIView, self).create(request, *args, **kwargs)
		except IntegrityError:
			return Response({"error": "The nemis number has already been used"})

class PupilDetail(RetrieveUpdateAPIView):
	"""
		Description
		-------------
			* A view which can be used to retrive detail information about a pupil and at the same time you can update it and delete it.

	"""
	serializer_class = PupilDetailSer
	queryset = Pupil.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolTeacher]


# Subject

class SubjectList(ListAPIView):
	"""
		Description
		-------------
			* A view which can be used to retrieve all the subjects in a the database
	"""

	serializer_class = SubjectListSer
	queryset = Subject.objects.all()


class SubjectDetail(RetrieveAPIView):
	"""	
		Description
		-------------
			* A view which provide detailed information about a single subject

		Constraints
		--------------
			* Cannot be created because it is managed by the admin, nor update, not delete

	"""

	serializer_class = SubjectDetailSer
	queryset = Subject.objects.all()




# Teacher

class TeacherCreate(CreateAPIView):
	"""
		Description
		-------------
			* A view which will be used to create a teacher into the system.

		Constraints
		-------------
			* This will be used in conjuction with registration process..
	"""
	serializer_class = TeacherCreateSer
	queryset = Teacher.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			data = serializer.data
		return super(TeacherCreate, self).create(request, *args, **kwargs)




class TeacherList(ListCreateAPIView):
	"""
		Description
		--------------
			* A view to retrieve teachers and you can also create a teacher
	"""
	serializer_class = TeacherListSer
	queryset = Teacher.objects.all()



class TeacherDetail(RetrieveUpdateDestroyAPIView):
	"""
		Description
		-------------
			* A view to retrieve detailed info about a teacher and you can also update information, and delete the teacher
	"""
	serializer_class = TeacherDetailSer
	queryset = Teacher.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolStaffTeacher]

