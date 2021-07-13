from rest_framework import serializers
from django.contrib.auth.models import User


# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=255, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'Error': 'Password1 and Password2 is different, please try again'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error': 'Email is does not exists.'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account