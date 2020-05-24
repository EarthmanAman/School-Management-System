from django.contrib import admin

from . models import (
	AssessType, 
	Assess, 
	Result,
	)

admin.site.register(AssessType)
admin.site.register(Assess)
admin.site.register(Result)