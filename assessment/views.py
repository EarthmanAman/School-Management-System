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
	)


class AssessTypeCreate(CreateAPIView):
	serializer_class = AssessTypeCreateSer
	queryset = AssessType.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class AssessTypeList(ListAPIView):

	serializer_class = AssessTypeListSer
	queryset = AssessType.objects.all()

class AssessTypeDetail(RetrieveUpdateAPIView):
	serializer_class = AssessTypeDetailSer
	queryset = AssessType.objects.all()
	permission_classes = [IsAuthenticated, IsClassTeacher_Assess_Type]




class AssessCreate(CreateAPIView):
	serializer_class = AssessCreateSer
	queryset = Assess.objects.all()
	permission_classes = [IsAuthenticated]

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class AssessList(ListAPIView):

	serializer_class = AssessListSer
	queryset = Assess.objects.all()

class AssessDetail(RetrieveUpdateAPIView):
	serializer_class = AssessDetailSer
	queryset = Assess.objects.all()
	permission_classes = [IsAuthenticated, IsSubjectTeacher_Assess]





class ResultCreate(CreateAPIView):
	serializer_class = ResultCreateSer
	queryset = Result.objects.all()

class ResultList(ListAPIView):

	serializer_class = ResultListSer
	queryset = Result.objects.all()

class ResultDetail(RetrieveUpdateAPIView):
	serializer_class = ResultDetailSer
	queryset = Result.objects.all()

	permission_classes = [IsAuthenticated, IsSubjectTeacher_Result]