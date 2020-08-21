from django.shortcuts import render

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.permissions import AllowAny, IsAuthenticated

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

from . permissions import (
	IsSchoolHead, 
	IsClassTeacher_Class, 
	IsSchoolStaffTeacher_Class,
	IsClassTeacher_Class_Pupil, 
	IsSchoolStaffTeacher_Class_Pupil
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
	permission_classes = [IsAuthenticated, IsSchoolHead]


# School Teacher

class SchoolGradeCreate(CreateAPIView):
	serializer_class = SchoolGradeCreateSer
	queryset = SchoolGrade.objects.all()
	permission_classes = [IsAuthenticated, IsSchoolHead]

class SchoolGradeList(ListAPIView):
	serializer_class = SchoolGradeListSer
	queryset = SchoolGrade.objects.all()

class SchoolGradeDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolGradeDetailSer
	queryset = SchoolGrade.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]


# School Teacher

class SchoolTeacherCreate(CreateAPIView):
	serializer_class = SchoolTeacherCreateSer
	queryset = SchoolTeacher.objects.all()
	permission_classes = [IsAuthenticated, IsSchoolHead]

class SchoolTeacherList(ListAPIView):
	serializer_class = SchoolTeacherListSer
	queryset = SchoolTeacher.objects.all()

class SchoolTeacherDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolTeacherDetailSer
	queryset = SchoolTeacher.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

# School Subject

class SchoolSubjectCreate(CreateAPIView):
	serializer_class = SchoolSubjectCreateSer
	queryset = SchoolSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

class SchoolSubjectList(ListAPIView):
	serializer_class = SchoolSubjectListSer
	queryset = SchoolSubject.objects.all()

class SchoolSubjectDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolSubjectDetailSer
	queryset = SchoolSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

# Grade Subject

class GradeSubjectCreate(CreateAPIView):
	serializer_class = GradeSubjectCreateSer
	queryset = GradeSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

class GradeSubjectList(ListAPIView):
	serializer_class = GradeSubjectListSer
	queryset = GradeSubject.objects.all()

class GradeSubjectDetail(RetrieveUpdateAPIView):
	serializer_class = GradeSubjectDetailSer
	queryset = GradeSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]



# Grade Class

class GradeClassCreate(CreateAPIView):
	serializer_class = GradeClassCreateSer
	queryset = GradeClass.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

class GradeClassList(ListAPIView):
	serializer_class = GradeClassListSer
	queryset = GradeClass.objects.all()

class GradeClassDetail(RetrieveUpdateAPIView):
	serializer_class = GradeClassDetailSer
	queryset = GradeClass.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead, ]



# Grade Pupil

class ClassPupilCreate(CreateAPIView):
	serializer_class = ClassPupilCreateSer
	queryset = ClassPupil.objects.all()
	permission_classes = [IsAuthenticated, IsClassTeacher_Class_Pupil]

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class ClassPupilList(ListAPIView):
	serializer_class = ClassPupilListSer
	queryset = ClassPupil.objects.all()

class ClassPupilDetail(RetrieveUpdateAPIView):
	serializer_class = ClassPupilDetailSer
	queryset = ClassPupil.objects.all()
	permission_classes = [IsAuthenticated, IsClassTeacher_Class_Pupil]