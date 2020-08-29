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

	SchoolGradeSubjectList,

	GradeClassCreate,
	GradeClassList,
	GradeClassDetail,

	SchoolGradeClassList,

	ClassPupilCreate,
	ClassPupilList,
	ClassPupilDetail,

	SchoolPupilList,
	)

app_name = "institution"

urlpatterns = [

    path('schools.json', SchoolList.as_view(), name="schools"),
    path('schools/<int:pk>.json', SchoolDetail.as_view(), name="schools_detail"),

    # School Grade
	path('grades/create.json', SchoolGradeCreate.as_view(), name="school_grades_create"),    
	path('<int:school_id>/grades.json', SchoolGradeList.as_view(), name="school_grades"),    
	path('<int:school_id>/grades/<int:pk>.json', SchoolGradeDetail.as_view(), name="school_grades_detail"),

    # School Teacher

    path('teachers/create.json', SchoolTeacherCreate.as_view(), name="school_teachers_create"),
    path('<int:school_id>/teachers.json', SchoolTeacherList.as_view(), name="school_teachers"),
    path('<int:school_id>/teachers/<int:pk>.json', SchoolTeacherDetail.as_view(), name="school_teachers_detail"),


    # School Subject

    path('subjects/create.json', SchoolSubjectCreate.as_view(), name="school_subjects_create"),
    path('<int:school_id>/subjects.json', SchoolSubjectList.as_view(), name="school_subjects"),
    path('<int:school_id>/subjects/<int:pk>.json', SchoolSubjectDetail.as_view(), name="school_subjects_detail"),


    # Grade Subject

    path('grade/subjects/create.json', GradeSubjectCreate.as_view(), name="grade_subjects_create"),
    path('<int:school_grade_id>/grade/subjects.json', GradeSubjectList.as_view(), name="grade_subjects"),
    path('<int:school_grade_id>/grade/subjects/<int:pk>.json', GradeSubjectDetail.as_view(), name="grade_subjects_detail"),

    path('<int:school_id>/school/grade/subjects.json', SchoolGradeSubjectList.as_view(), name="school_grade_subjects"),
    # Grade Class

    path('grade/classes/create.json', GradeClassCreate.as_view(), name="grade_classes_create"),
    path('<int:school_grade_id>/grade/classes.json', GradeClassList.as_view(), name="grade_classes"),
    path('<int:school_grade_id>/grade/classes/<str:name>.json', GradeClassDetail.as_view(), name="grade_classes_detail"),

    path('<int:school_id>/school/classes.json', SchoolGradeClassList.as_view(), name="schoo_grade_classes"),
    # Class Pupil

    path('class/pupils/create.json', ClassPupilCreate.as_view(), name="class_pupils_create"),
    path('<int:class_id>/class/pupils.json', ClassPupilList.as_view(), name="class_pupils"),
    path('<int:class_id>/class/pupils/<int:pk>.json', ClassPupilDetail.as_view(), name="class_pupils_detail"),

    path('<int:school_id>/school/pupils.json', SchoolPupilList.as_view(), name="school_pupils"),

]
