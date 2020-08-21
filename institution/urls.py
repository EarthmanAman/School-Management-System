from django.urls import path

from . views import (
	SchoolList,
	SchoolDetail,
	SchoolTeacherCreate,
	SchoolTeacherList,
	SchoolTeacherDetail,

	SchoolGradeCreate,
	SchoolGradeList,
	SchoolGradeDetail,

	SchoolSubjectCreate,
	SchoolSubjectList,
	SchoolSubjectDetail,

	GradeSubjectCreate,
	GradeSubjectList,
	GradeSubjectDetail,

	GradeClassCreate,
	GradeClassList,
	GradeClassDetail,

	ClassPupilCreate,
	ClassPupilList,
	ClassPupilDetail,
	)

app_name = "institution"

urlpatterns = [

    path('schools.json', SchoolList.as_view(), name="schools"),
    path('schools/<int:pk>.json', SchoolDetail.as_view(), name="schools_detail"),

    # School Grade
	path('school_grades/create.json', SchoolGradeCreate.as_view(), name="school_grades_create"),    
	path('school_grades.json', SchoolGradeList.as_view(), name="school_grades"),    
	path('school_grades/<int:pk>.json', SchoolGradeDetail.as_view(), name="school_grades_detail"),

    # School Teacher

    path('school_teachers/create.json', SchoolTeacherCreate.as_view(), name="school_teachers_create"),
    path('school_teachers.json', SchoolTeacherList.as_view(), name="school_teachers"),
    path('school_teachers/<int:pk>.json', SchoolTeacherDetail.as_view(), name="school_teachers_detail"),


    # School Subject

    path('school_subjects/create.json', SchoolSubjectCreate.as_view(), name="school_subjects_create"),
    path('school_subjects.json', SchoolSubjectList.as_view(), name="school_subjects"),
    path('school_subjects/<int:pk>.json', SchoolSubjectDetail.as_view(), name="school_subjects_detail"),


    # Grade Subject

    path('grade_subjects/create.json', GradeSubjectCreate.as_view(), name="grade_subjects_create"),
    path('grade_subjects.json', GradeSubjectList.as_view(), name="grade_subjects"),
    path('grade_subjects/<int:pk>.json', GradeSubjectDetail.as_view(), name="grade_subjects_detail"),

    # Grade Class

    path('grade_classes/create.json', GradeClassCreate.as_view(), name="grade_classes_create"),
    path('grade_classes.json', GradeClassList.as_view(), name="grade_classes"),
    path('grade_classes/<int:pk>.json', GradeClassDetail.as_view(), name="grade_classes_detail"),

    # Class Pupil

    path('class_pupils/create.json', ClassPupilCreate.as_view(), name="class_pupils_create"),
    path('class_pupils.json', ClassPupilList.as_view(), name="class_pupils"),
    path('class_pupils/<int:pk>.json', ClassPupilDetail.as_view(), name="class_pupils_detail"),

]
