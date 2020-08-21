from rest_framework.permissions import BasePermission, SAFE_METHODS

from institution.models import SchoolTeacher

from . models import AssessType, Assess, Result


class IsSchoolStaff_Assess_Type(BasePermission):

	def has_object_permission(self, request, view, obj):
		school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)

		for school_teacher in school_teachers:
			if school_teacher in obj.school_grade.school.schoolteacher_set.all() and request.method in SAFE_METHODS:
				return True

		return request.user.is_superuser

class IsSubjectTeacher_Assess(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			for school_teacher in school_teachers:
				if school_teacher == obj.grade_subject.subject_teacher:
					return True
				elif school_teacher in obj.grade_subject.school_grade.class_teachers():
					return True
				elif heads.exists():
					for head in heads:
						if head.school == obj.grade_subject.school_grade.school:
							return True

			return request.user.is_superuser
		except:
			return request.user.is_superuser

class IsSubjectTeacher_Result(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")

			for school_teacher in school_teachers:
				if school_teacher == obj.assess.grade_subject.subject_teacher:
					return True
				elif school_teacher in obj.assess.grade_subject.school_grade.class_teachers():
					return True
				elif heads.exists():
					for head in heads:
						if head.school == obj.assess.grade_subject.school_grade.school:
							return True

			return request.user.is_superuser
		except:
			return request.user.is_superuser
class IsClassTeacher_Assess_Type(BasePermission):

	def has_object_permission(self, request, view, obj):
		try:
			
			school_teachers = SchoolTeacher.objects.filter(teacher=request.user.teacher)
			heads = school_teachers.filter(position="ht")
			class_teachers = obj.school_grade.class_teachers()

			for school_teacher in school_teachers:
				if school_teacher in class_teachers:
					return True

			if heads.exists():
				
				for head in heads:
					if head.school == obj.school_grade.school:
						return True


			return request.user.is_superuser

		except:

			return request.user.is_superuser