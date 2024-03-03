from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

        extra_kwargs = {'password': {'write_only': True}}


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # first_name = serializers.CharField(style={'input_type': 'first_name'})
    # last_name = serializers.CharField(style={'input_type': 'last_name'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

        extra_kwargs = {'password': {'write_only': True}}

        
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must mutch'})

        user.set_password(password)
        user.save()
        return user





# class RegisterUserSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True)
#     first_name = serializers.CharField(style={'input_type': 'first_name'})

#     class Meta:
#         model = User
#         fields = ('first_name', 'email', 'username', 'password1', 'password2')

#     def validate(self, attrs):
#         if attrs['password1'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Passwords must match!"})

#         return attrs
        
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name']
#         )

#         user.set_password(validated_data['password1'])
#         user.save()

#         return user







# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance