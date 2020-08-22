from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
	message = "You dont have authorization to perform this action"
	def has_object_permission(self, request, view, obj):

		if obj == request.user:
			return True
		else:
			return request.user.is_superuser


