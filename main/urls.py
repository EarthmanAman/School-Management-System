from django.urls import path

from . views import (
	GradeList, 
	GradeDetail,

	PupilList, 
	PupilDetail,


	SubjectList,
	SubjectDetail,

	TeacherCreate,
	TeacherList,
	TeacherDetail,
	)

app_name = "main"

urlpatterns = [

    path('grades.json', GradeList.as_view(), name="grades"),
    path('grades/<int:pk>.json', GradeDetail.as_view(), name="grades_detail"),

    path('pupils.json', PupilList.as_view(), name="pupils"),
    path('pupils/<int:pk>.json', PupilDetail.as_view(), name="pupils_detail"),
   

    path('subjects.json', SubjectList.as_view(), name="subjects"),
    path('subjects/<int:pk>.json', SubjectDetail.as_view(), name="subjects_detail"),

    path('teachers/create.json', TeacherCreate.as_view(), name="teachers_create"),
    path('teachers.json', TeacherList.as_view(), name="teachers"),
    path('teachers/<int:pk>.json', TeacherDetail.as_view(), name="teachers_detail"),
]
