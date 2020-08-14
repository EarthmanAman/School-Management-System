from django.urls import path

from . views import (
	AssessTypeCreate,
	AssessTypeList,
	AssessTypeDetail,

	AssessCreate,
	AssessList,
	AssessDetail,

	ResultCreate,
	ResultList,
	ResultDetail,
	)

app_name = "assessment"

urlpatterns = [

    path('assess_types/create.json', AssessTypeCreate.as_view(), name="assess_types_create"),
    path('assess_types.json', AssessTypeList.as_view(), name="assess_types"),
    path('assess_types/<int:pk>.json', AssessTypeDetail.as_view(), name="assess_types_detail"),


    path('assess/create.json', AssessCreate.as_view(), name="assess_create"),
    path('assess.json', AssessList.as_view(), name="assess"),
    path('assess/<int:pk>.json', AssessDetail.as_view(), name="assess_detail"),


    path('result/create.json', ResultCreate.as_view(), name="result_create"),
    path('result.json', ResultList.as_view(), name="result"),
    path('result/<int:pk>.json', ResultDetail.as_view(), name="result_detail"),
  
]
