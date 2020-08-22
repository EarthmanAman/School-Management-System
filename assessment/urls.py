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

	SubjectAssess,
	SubjectAssessDetail,

	AssessTypePupilList,
	AssessTypePupilDetail,
	AssessPupilList,

	AssessTypeMin,
	AssessTypeMinDetail,

	AssessMinList,
	AssessMinDetail,

	AssessPupilMinList,
	AssessPupilMinDetail,
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
  	

  	path('<int:assess_type_id>/<int:grade_subject_id>/subject/assess.json', SubjectAssess.as_view(), name="subject_assess"),
  	path('<int:assess_type_id>/<int:grade_subject_id>/subject/detail.json', SubjectAssessDetail.as_view(), name="subject_assess_detail"),

  	path('<int:pupil_nemis_no>/results.json', AssessTypePupilList.as_view(), name="assess_type_pupil"),
  	path('<int:pupil_nemis_no>/<int:pk>/results.json', AssessTypePupilDetail.as_view(), name="assess_type_pupil_detail"),
  	path('<int:grade_subject_id>/<int:pupil_nemis_no>/results.json', AssessPupilList.as_view(), name="assess_pupil"),

  	path('<int:school_grade_id>/results/min.json', AssessTypeMin.as_view(), name="assess_type_min"),
  	path('<int:school_grade_id>/<int:pk>/results/min.json', AssessTypeMinDetail.as_view(), name="assess_type_min_detail"),

  	path('<int:school_grade_id>/<int:grade_subject_id>/subject/min.json', AssessMinList.as_view(), name="assess_min"),
  	path('<int:school_grade_id>/<int:grade_subject_id>/<int:pk>/subject/min.json', AssessMinDetail.as_view(), name="assess_min_detail"),

  	path('<int:school_grade_id>/pupils/min.json', AssessPupilMinList.as_view(), name="assess_pupils_min"),
  	path('<int:school_grade_id>/<int:pk>/pupils/min.json', AssessPupilMinDetail.as_view(), name="assess_pupils_min_detail"),
]
