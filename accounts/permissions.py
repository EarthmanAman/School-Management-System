from rest_framework.permissions import BasePermission


class IsUserOrReadOnly(BasePermission):

	def has_object_permission(self, request, view, obj):
		return obj == request.user or request.user.is_superuser 


class IsSchoolStaff(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			
			return obj.teacher.schoolteacher.school == request.user.teacher.schoolteacher.school or obj.is_superuser or obj.is_staff

		except:

			return False