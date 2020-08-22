from django.shortcuts import render


from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from institution.models import ClassPupil, GradeSubject, SchoolGrade

from . models import (
	AssessType,
	Assess,
	Result,
	)

from . permissions import (
	IsClassTeacher_Assess_Type, 
	IsSchoolStaff_Assess_Type, 
	IsSubjectTeacher_Assess, 
	IsSubjectTeacher_Result,
	)

from . serializers import (
	
	AssessTypeCreateSer,
	AssessTypeListSer,
	AssessTypeDetailSer,

	AssessCreateSer,
	AssessListSer,
	AssessDetailSer,

	ResultCreateSer,
	ResultListSer,
	ResultDetailSer,

	AssessTypePupilListSer,

	AssessPupilListSer,
	AssessTypeMinSer,
	AssessMinSer,
	AssessPupilsMinSer,

	SubjectAssessDetailSer,
	)


class AssessTypeCreate(CreateAPIView):
	serializer_class = AssessTypeCreateSer

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class AssessTypeList(ListAPIView):

	serializer_class = AssessTypeListSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return AssessType.objects.assess_types(int(school_grade_id))

class AssessTypeDetail(RetrieveUpdateAPIView):
	serializer_class = AssessTypeDetailSer
	queryset = AssessType.objects.all()
	permission_classes = [IsAuthenticated, IsClassTeacher_Assess_Type]

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return AssessType.objects.assess_types(int(school_grade_id))
		
class AssessTypePupilList(ListAPIView):
	serializer_class = AssessTypePupilListSer

	def get_queryset(self, *args, **kwargs):
		pupil_nemis_no = self.kwargs.get("pupil_nemis_no")
		class_pupil = ClassPupil.objects.get(pupil__nemis_no=int(pupil_nemis_no))
		return class_pupil.grade_class.school_grade.assesstype_set.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request, "pupil_nemis_no": self.kwargs.get("pupil_nemis_no")}

class AssessTypePupilDetail(RetrieveAPIView):
	serializer_class = AssessTypePupilListSer

	def get_queryset(self, *args, **kwargs):
		pupil_nemis_no = self.kwargs.get("pupil_nemis_no")
		class_pupil = ClassPupil.objects.get(pupil__nemis_no=int(pupil_nemis_no))
		return class_pupil.grade_class.school_grade.assesstype_set.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request, "pupil_nemis_no": self.kwargs.get("pupil_nemis_no")}

class AssessTypeMin(ListAPIView):
	serializer_class = AssessTypeMinSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		school_grade = SchoolGrade.objects.get(id=school_grade_id)

		return school_grade.assesstype_set.all()

class AssessTypeMinDetail(RetrieveAPIView):
	serializer_class = AssessTypeMinSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		school_grade = SchoolGrade.objects.get(id=school_grade_id)

		return school_grade.assesstype_set.all()


class AssessCreate(CreateAPIView):
	serializer_class = AssessCreateSer
	queryset = Assess.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class AssessList(ListAPIView):

	serializer_class = AssessListSer
	queryset = Assess.objects.all()

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return Assess.objects.assesses(int(school_grade_id))
		
class AssessDetail(RetrieveUpdateAPIView):
	serializer_class = AssessDetailSer
	queryset = Assess.objects.all()
	permission_classes = [IsAuthenticated, IsSubjectTeacher_Assess]

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		return Assess.objects.assesses(int(school_grade_id))


class SubjectAssess(ListAPIView):

	serializer_class = AssessListSer

	def get_queryset(self, *args, **kwargs):
		assess_type_id = self.kwargs.get("assess_type_id")
		grade_subject_id = self.kwargs.get("grade_subject_id")
		return Assess.objects.subject_assesses(int(assess_type_id), int(grade_subject_id))

class SubjectAssessDetail(ListAPIView):

	serializer_class = SubjectAssessDetailSer

	def get_queryset(self, *args, **kwargs):
		assess_type_id = self.kwargs.get("assess_type_id")
		grade_subject_id = self.kwargs.get("grade_subject_id")
		return Assess.objects.subject_assesses(int(assess_type_id), int(grade_subject_id))

class AssessMinList(ListAPIView):
	serializer_class = AssessMinSer

	def get_queryset(self, *args, **kwargs):
		grade_subject_id = self.kwargs.get("grade_subject_id")
		grade_subject = GradeSubject.objects.get(id=grade_subject_id)

		return grade_subject.assess_set.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"school_grade_id":self.kwargs.get("school_grade_id")}

class AssessMinDetail(RetrieveAPIView):
	serializer_class = AssessMinSer

	def get_queryset(self, *args, **kwargs):
		grade_subject_id = self.kwargs.get("grade_subject_id")
		grade_subject = GradeSubject.objects.get(id=grade_subject_id)

		return grade_subject.assess_set.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"school_grade_id":self.kwargs.get("school_grade_id")}


class AssessPupilMinList(ListAPIView):
	serializer_class = AssessPupilsMinSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		

		return AssessType.objects.filter(school_grade__id=school_grade_id)

	def get_serializer_context(self, *args, **kwargs):
		return {"school_grade_id":self.kwargs.get("school_grade_id")}

class AssessPupilMinDetail(RetrieveAPIView):
	serializer_class = AssessPupilsMinSer

	def get_queryset(self, *args, **kwargs):
		school_grade_id = self.kwargs.get("school_grade_id")
		

		return AssessType.objects.filter(school_grade__id=school_grade_id)

	def get_serializer_context(self, *args, **kwargs):
		return {"school_grade_id":self.kwargs.get("school_grade_id")}










class AssessPupilList(ListAPIView):
	serializer_class = AssessPupilListSer

	def get_queryset(self, *args, **kwargs):
		grade_subject_id = self.kwargs.get("grade_subject_id")
		grade_subject = GradeSubject.objects.get(pk=int(grade_subject_id))
		pupil_nemis_no = self.kwargs.get("pupil_nemis_no")
		results = Result.objects.filter(pupil__nemis_no=pupil_nemis_no)
		results = results.filter(assess__grade_subject=grade_subject)
		return results

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request, "pupil_nemis_no": self.kwargs.get("pupil_nemis_no")}




class ResultCreate(CreateAPIView):
	serializer_class = ResultCreateSer
	queryset = Result.objects.all()

class ResultList(ListAPIView):

	serializer_class = ResultListSer

	def get_queryset(self, *args, **kwargs):
		assess_id = self.kwargs.get("assess_id")
		return Result.objects.results(int(assess_id))


class ResultDetail(RetrieveUpdateAPIView):
	serializer_class = ResultDetailSer

	permission_classes = [IsAuthenticated, IsSubjectTeacher_Result]

	def get_queryset(self, *args, **kwargs):
		assess_id = self.kwargs.get("assess_id")
		return Result.objects.results(int(assess_id))

