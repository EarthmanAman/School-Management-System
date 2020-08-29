from rest_framework.permissions import BasePermission, SAFE_METHODS
from institution.models import SchoolTeacher

class IsSchoolStaffTeacher(BasePermission):
	message = "You dont have authorization to perform this action"
	def has_object_permission(self, request, view, obj):
		if obj.user == request.user:
			return True
		try:
			
			return obj.schoolteacher_set.first().school == request.user.teacher.schoolteacher_set.first().school and request.method in SAFE_METHODS
		except:
			
			return request.user.is_superuser 




class IsSchoolHeadTeacher(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			school_teachers = SchoolTeacher.objects.filter(teacher__user=request.user)
			school_heads = request.user.teacher.schoolteacher_set.filter(position="ht")

			if school_teachers.exists() and school_heads.exists() and request.method in SAFE_METHODS:
				
				for school_head in school_heads:

					if school_head in school_teachers:
						return True
			elif request.user == obj.user:
				return True

			return request.user.is_superuser
		except:
			return request.user.is_superuser

