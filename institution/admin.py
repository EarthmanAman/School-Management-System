from django.contrib import admin

from . models import (
	School, 
	SchoolTeacher, 
	SchoolGrade, 
	SchoolSubject, 
	GradeSubject, 
	GradeClass, 
	ClassPupil,
	)

admin.site.register(School)
admin.site.register(SchoolTeacher)
admin.site.register(SchoolGrade)
admin.site.register(SchoolSubject)
admin.site.register(GradeSubject)
admin.site.register(GradeClass)
admin.site.register(ClassPupil)