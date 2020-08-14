from rest_framework.permissions import BasePermission, SAFE_METHODS

from . models import SchoolTeacher

class IsSchoolTeacher(BasePermission):

	message = "You dont have authorization to perform this action"

	def has_object_permission(self, request, view, obj):
		try:
			school_teacher = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			if school_teacher.exists() or request.user.is_superuser or request.method in SAFE_METHODS:
				return True
			else:
				return False
		except:
			return False



class IsSchoolStaff(BasePermission):
	message = "You dont have authorization to perform this action"
	def has_object_permission(self, request, view, obj):
		if obj == request.user:
			return True
		try:
			return obj.teacher.schoolteacher_set.first().school == request.user.teacher.schoolteacher_set.first().school and request.method in SAFE_METHODS
		except:

			return request.user.is_superuser 




