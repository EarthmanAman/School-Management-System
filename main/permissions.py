from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSchoolStaffTeacher(BasePermission):
	message = "You dont have authorization to perform this action"
	def has_object_permission(self, request, view, obj):
		if obj.user == request.user:
			return True
		try:
			
			return obj.schoolteacher_set.first().school == request.user.teacher.schoolteacher_set.first().school and request.method in SAFE_METHODS
		except:
			
			return request.user.is_superuser 




