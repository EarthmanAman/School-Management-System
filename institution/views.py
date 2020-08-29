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
	IsSchoolHead_School_Teacher,
	IsSchoolStaffTeacher_Grade,
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

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolGrade.objects.school_grades(int(school_id))

class SchoolGradeDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolGradeDetailSer

	permission_classes = [IsAuthenticated, IsSchoolStaffTeacher_Grade]

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolGrade.objects.school_grades(int(school_id))


# School Teacher

class SchoolTeacherCreate(CreateAPIView):
	serializer_class = SchoolTeacherCreateSer
	queryset = SchoolTeacher.objects.all()
	permission_classes = [IsAuthenticated, IsSchoolHead]

class SchoolTeacherList(ListAPIView):
	serializer_class = SchoolTeacherListSer

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolTeacher.objects.school_teachers(int(school_id))

class SchoolTeacherDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolTeacherDetailSer

	permission_classes = [IsAuthenticated, IsSchoolHead_School_Teacher]

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolTeacher.objects.school_teachers(int(school_id))

# School Subject

class SchoolSubjectCreate(CreateAPIView):
	serializer_class = SchoolSubjectCreateSer
	queryset = SchoolSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

	
class SchoolSubjectList(ListAPIView):
	serializer_class = SchoolSubjectListSer

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolSubject.objects.school_subjects(int(school_id))

class SchoolSubjectDetail(RetrieveUpdateAPIView):
	serializer_class = SchoolSubjectDetailSer

	permission_classes = [IsAuthenticated, IsSchoolHead_School_Teacher]

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return SchoolSubject.objects.school_subjects(int(school_id))

# Grade Subject

class GradeSubjectCreate(CreateAPIView):
	serializer_class = GradeSubjectCreateSer
	queryset = GradeSubject.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

class GradeSubjectList(ListAPIView):
	serializer_class = GradeSubjectListSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return GradeSubject.objects.grade_subjects(int(school_grade_id))

class GradeSubjectDetail(RetrieveUpdateAPIView):
	serializer_class = GradeSubjectDetailSer

	permission_classes = [IsAuthenticated, IsSchoolHead]

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return GradeSubject.objects.grade_subjects(int(school_grade_id))


class SchoolGradeSubjectList(ListAPIView):
	serializer_class = GradeSubjectListSer

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return GradeSubject.objects.filter(school_grade__school__id=int(school_id))

# Grade Class

class GradeClassCreate(CreateAPIView):
	serializer_class = GradeClassCreateSer
	queryset = GradeClass.objects.all()

	permission_classes = [IsAuthenticated, IsSchoolHead]

class GradeClassList(ListAPIView):
	serializer_class = GradeClassListSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return GradeClass.objects.grade_classes(int(school_grade_id))

class GradeClassDetail(RetrieveUpdateAPIView):
	serializer_class = GradeClassDetailSer

	permission_classes = [IsAuthenticated, IsSchoolHead, ]
	lookup_field = "name"
	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return GradeClass.objects.grade_classes(int(school_grade_id))

class SchoolGradeClassList(ListAPIView):
	serializer_class = GradeClassListSer

	def get_queryset(self, *args, **kwargs):
		school_id = self.kwargs.get("school_id")
		return GradeClass.objects.filter(school_grade__school__id=int(school_id))


# Grade Pupil

class ClassPupilCreate(CreateAPIView):
	serializer_class = ClassPupilCreateSer
	queryset = ClassPupil.objects.all()
	permission_classes = [IsAuthenticated, IsClassTeacher_Class_Pupil]

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class ClassPupilList(ListAPIView):
	serializer_class = ClassPupilListSer

	def get_queryset(self, *args, **kwargs):
		class_id = self.kwargs.get("class_id")
		return ClassPupil.objects.class_pupils(int(class_id))

class SchoolPupilList(ListAPIView):
	serializer_class = ClassPupilListSer

	def get_queryset(self, *args, **kwargs):
		class_id = self.kwargs.get("school_id")
		return ClassPupil.objects.filter(grade_class__school_grade__school__id=int(class_id))

class ClassPupilDetail(RetrieveUpdateAPIView):
	serializer_class = ClassPupilDetailSer
	
	permission_classes = [IsAuthenticated, IsClassTeacher_Class_Pupil]

	def get_queryset(self, *args, **kwargs):
		class_id = self.kwargs.get("class_id")
		return ClassPupil.objects.class_pupils(int(class_id))

