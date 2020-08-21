from rest_framework.permissions import BasePermission, SAFE_METHODS

from . models import SchoolTeacher

class IsSchoolTeacher(BasePermission):

	message = "You dont have authorization to perform this action"

	def has_permission(self, request, view):
		try:
			school_teacher = SchoolTeacher.objects.filter(teacher__user=request.user)
			if school_teacher.exists() or request.user.is_superuser:
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




class IsSchoolHead(BasePermission):

	def has_permission(self, request, view):
		try:
			school_teachers = SchoolTeacher.objects.filter(teacher__user=request.user)
			school_heads = request.user.teacher.schoolteacher_set.filter(position="ht")

			if school_teachers.exists() and school_heads.exists():
				
				for school_head in school_heads:

					if school_head in school_teachers:
						return True
			elif request.method in SAFE_METHODS:
				return True

			return request.user.is_superuser
		except:
			return request.user.is_superuser


class IsClassTeacher_Class(BasePermission):

	def has_object_permission(self, request, view, obj):
		school_teachers = request.user.teacher.schoolteacher_set()
		if obj.class_teacher in school_teachers:
			return True
		elif [True for school_t in school_teachers if school_t["position"]== "ht"]:
			return True
		return request.user.is_superuser

class IsSchoolStaffTeacher_Class_Pupil(BasePermission):

	def has_object_permission(self, request, view, obj):
		print("In hereee")
		try:

			school_teachers = request.user.teacher.schoolteacher_set()
			if obj.grade_class.class_teacher in school_teachers:
				return True
			elif [True for school_t in school_teachers if school_t["position"]== "ht"]:
				return True
			return request.user.is_superuser
		except:
			return request.user.is_superuser



class IsSchoolStaffTeacher_Class(BasePermission):
	message = "You dont have authorization to perform this action"
	def has_object_permission(self, request, view, obj):
		try:
			if request.method in SAFE_METHODS:
				return [True for school_teacher in request.user.teacher.schoolteacher_set() if obj.class_teacher.school_teacher.school == school_teacher.school]
			else:
				return [True for school_teacher in request.user.teacher.schoolteacher_set() if obj.class_teacher.school_teacher == school_teacher] or [True for school_teacher in  request.user.teacher.schoolteacher_set() if obj.class_teacher.school_teacher == request.user.teacher.school_teacher.school.get_head()]
		except:
			
			return request.user.is_superuser 



class IsClassTeacher_Class_Pupil(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			if obj.grade_class.class_teacher in school_teachers:
				return True

			if heads.exists():
				
				for head in heads:
					if head.school == obj.grade_class.class_teacher.school:
						return True


			return request.user.is_superuser

		except:

			return request.user.is_superuser