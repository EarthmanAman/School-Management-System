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
    path('<int:school_grade_id>/assess/types.json', AssessTypeList.as_view(), name="assess_types"),
    path('<int:school_grade_id>/assess/types/<int:pk>.json', AssessTypeDetail.as_view(), name="assess_types_detail"),


    path('assess/create.json', AssessCreate.as_view(), name="assess_create"),
    path('<int:school_grade_id>/assess.json', AssessList.as_view(), name="assess"),
    path('<int:school_grade_id>/assess/<int:pk>.json', AssessDetail.as_view(), name="assess_detail"),


    path('result/create.json', ResultCreate.as_view(), name="result_create"),
    path('<int:assess_id>/result.json', ResultList.as_view(), name="result"),
    path('<int:assess_id>/result/<int:pk>.json', ResultDetail.as_view(), name="result_detail"),
  
]
