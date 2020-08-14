from django.core.exceptions import ValidationError

def validate_id_no(value):
	if type(value) != int:
		raise ValidationError(
				("ID number must be a number"),
				params={"value":value},
			)