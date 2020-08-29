from django.contrib.auth.models import User

from rest_framework.serializers import (
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer, 
	SerializerMethodField,
	ListField,

	ValidationError,	
	)

class UserSer(ModelSerializer):

	"""
		Description
		-------------
			* Serializer for the User Model
			* Handle detailed info about a user

		Variables
		----------
			* No variables

		Fields
		---------
			id
			username
			first_name
			last_name
			email

		Methods
		--------

	"""

	class Meta:
		model = User
		fields = [
			"id",
			"username",
			"first_name",
			"last_name",
			"email",

		]

class UserSerDetail(ModelSerializer):

	"""
		Description
		-------------
			* Serializer for the User Model
			* Handle detailed info about a user

		Variables
		----------
			* No variables

		Fields
		---------
			id
			username
			first_name
			last_name
			email

		Methods
		--------

	"""

	class Meta:
		model = User
		fields = [
			"email",
			"first_name",
			"last_name",

		]

	def update(self, instance, validated_data):

		if instance.username != validated_data.get("email", instance.username):
			instance.username = validated_data["email"]

		instance.email = validated_data.get("email", instance.email)
		instance.first_name = validated_data.get("first_name", instance.first_name)
		instance.last_name = validated_data.get("last_name", instance.last_name)
		instance.save()
		return instance

class UserCreateSer(ModelSerializer):

	"""
		Description
		-------------
			* Serializer for the User Model
			* Handle creation of users

		Variables
		----------
			* email
			* email2

		Fields
		---------
			email
			email2
			first_name
			last_name
			password

		Methods
		--------
			* def validate_email2(self, value) = validate if email are equal
			* def create(self, data) = handle creation

	"""

	email = EmailField(label="Email Address")
	confirm_email = EmailField(label="Confirm Email")
	class Meta:
		model = User
		fields = [

			'email',
			'confirm_email',
			'first_name',
			'last_name',
			'password',
		]

		extra_kwargs = {'password':
			{"write_only":True}
		}
	
	def validate_confirm_email(self, value):
		data = self.get_initial()
		email = data.get('email')
		confirm_email = value

		if email != confirm_email:
			raise ValidationError("Emails Must Match.")

		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("This email is already registered.")
		return value

	def create(self, validated_data):
		email = validated_data['confirm_email']
		password = validated_data['password']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		user = User(username=email, email=email, first_name=first_name, last_name=last_name)
		user.set_password(password)
		user.save()
		return validated_data
