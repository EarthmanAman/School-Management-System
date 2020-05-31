from django.shortcuts import render

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from . models import Grade, Pupil, Subject, Teacher

from . serializers import (
	GradeListSer, 
	GradeDetailSer,
	PupilListSer, 
	PupilDetailSer,
	SubjectListSer,
	SubjectDetailSer,
)

"""
	APIS
	------
		GradeList ( /grades.json )
		----------------------------
			*Display all the main grades

		GradeDetail (/grades/<int:pk>.json)
		------------------------------------
			* Display detailed info dor a grade



		PupilList ( /pupils.json )
		----------------------------
			* Display all the pupils
			* Allow creation of a pupil

		PupilDetail (/pupils/<int:pk>.json)
		-------------
			* Return detailed information about a pupil



		SubjectList (/subjects.json)
		------------------------------
			* Display a list of all Subjects

		SubjectDetail (/subjects/<int:pk>.json)
		----------------------------------------
			* Return detailed info about a specified subject


"""

class GradeList(ListAPIView):

	serializer_class = GradeListSer
	queryset = Grade.objects.all()

class GradeDetail(RetrieveUpdateAPIView):
	serializer_class = GradeDetailSer
	queryset = Grade.objects.all()

class PupilList(ListCreateAPIView):

	serializer_class = PupilListSer
	queryset = Pupil.objects.all()

class PupilDetail(RetrieveUpdateAPIView):
	serializer_class = PupilDetailSer
	queryset = Pupil.objects.all()

class SubjectList(ListCreateAPIView):

	serializer_class = SubjectListSer
	queryset = Subject.objects.all()

class SubjectDetail(RetrieveUpdateAPIView):
	serializer_class = SubjectDetailSer
	queryset = Subject.objects.all()
