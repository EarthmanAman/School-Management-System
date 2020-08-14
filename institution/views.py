from django.shortcuts import render

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
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

from . serializers import (
	SchoolListSer,
	SchoolDetailSer,

	SchoolGradeCreateSer,
	SchoolGradeListSer,
	SchoolGradeDetailSer,

	SchoolTeacherCreateSer,
	SchoolTeacherListSer,
	SchoolTeacherDetailSer,

	# School Subject 
	SchoolSubjectCreateSer,
	SchoolSubjectListSer,
	SchoolSubjectDetailSer,

	# Grade Subject
	GradeSubjectCreateSer,
	GradeSubjectListSer,
	GradeSubjectDetailSer,

	# Grade Class
	GradeClassCreateSer,
	GradeClassListSer,
	GradeClassDetailSer,

	# Class Pupil
	ClassPupilCreateSer,
	ClassPupilListSer,
	ClassPupilDetailSer,
	)


class SchoolList(ListCreateAPIView):

	serializer_class = SchoolListSer
	queryset = School.objects.all()


class SchoolDetail(RetrieveUpdateAPIView):

	serializer_class = SchoolDetailSer
	queryset = School.objects.all()


# School Teacher

class SchoolGradeCreate(CreateAPIView):
	serializer_class = SchoolGradeCreateSer
	queryset = SchoolGrade.objects.all()

class SchoolGradeList(ListAPIView):
	serializer_class = SchoolGradeListSer
	queryset = SchoolGrade.objects.all()

class SchoolGradeDetail(RetrieveAPIView):
	serializer_class = SchoolGradeDetailSer
	queryset = SchoolGrade.objects.all()


# School Teacher

class SchoolTeacherCreate(CreateAPIView):
	serializer_class = SchoolTeacherCreateSer
	queryset = SchoolTeacher.objects.all()

class SchoolTeacherList(ListAPIView):
	serializer_class = SchoolTeacherListSer
	queryset = SchoolTeacher.objects.all()

class SchoolTeacherDetail(RetrieveAPIView):
	serializer_class = SchoolTeacherDetailSer
	queryset = SchoolTeacher.objects.all()


# School Subject

class SchoolSubjectCreate(CreateAPIView):
	serializer_class = SchoolSubjectCreateSer
	queryset = SchoolSubject.objects.all()

class SchoolSubjectList(ListAPIView):
	serializer_class = SchoolSubjectListSer
	queryset = SchoolSubject.objects.all()

class SchoolSubjectDetail(RetrieveAPIView):
	serializer_class = SchoolSubjectDetailSer
	queryset = SchoolSubject.objects.all()


# Grade Subject

class GradeSubjectCreate(CreateAPIView):
	serializer_class = GradeSubjectCreateSer
	queryset = GradeSubject.objects.all()

class GradeSubjectList(ListAPIView):
	serializer_class = GradeSubjectListSer
	queryset = GradeSubject.objects.all()

class GradeSubjectDetail(RetrieveAPIView):
	serializer_class = GradeSubjectDetailSer
	queryset = GradeSubject.objects.all()



# Grade Class

class GradeClassCreate(CreateAPIView):
	serializer_class = GradeClassCreateSer
	queryset = GradeClass.objects.all()

class GradeClassList(ListAPIView):
	serializer_class = GradeClassListSer
	queryset = GradeClass.objects.all()

class GradeClassDetail(RetrieveAPIView):
	serializer_class = GradeClassDetailSer
	queryset = GradeClass.objects.all()



# Grade Pupil

class ClassPupilCreate(CreateAPIView):
	serializer_class = ClassPupilCreateSer
	queryset = ClassPupil.objects.all()

class ClassPupilList(ListAPIView):
	serializer_class = ClassPupilListSer
	queryset = ClassPupil.objects.all()

class ClassPupilDetail(RetrieveAPIView):
	serializer_class = ClassPupilDetailSer
	queryset = ClassPupil.objects.all()