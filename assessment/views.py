from django.shortcuts import render


from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from . models import (
	AssessType,
	Assess,
	Result,
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

class AssessTypeList(ListAPIView):

	serializer_class = AssessTypeListSer
	queryset = AssessType.objects.all()

class AssessTypeDetail(RetrieveAPIView):
	serializer_class = AssessTypeDetailSer
	queryset = AssessType.objects.all()




class AssessCreate(CreateAPIView):
	serializer_class = AssessCreateSer
	queryset = Assess.objects.all()

class AssessList(ListAPIView):

	serializer_class = AssessListSer
	queryset = Assess.objects.all()

class AssessDetail(RetrieveAPIView):
	serializer_class = AssessDetailSer
	queryset = Assess.objects.all()





class ResultCreate(CreateAPIView):
	serializer_class = ResultCreateSer
	queryset = Result.objects.all()

class ResultList(ListAPIView):

	serializer_class = ResultListSer
	queryset = Result.objects.all()

class ResultDetail(RetrieveAPIView):
	serializer_class = ResultDetailSer
	queryset = Result.objects.all()