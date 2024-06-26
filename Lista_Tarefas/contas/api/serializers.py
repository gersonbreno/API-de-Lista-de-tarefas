from rest_framework import serializers
from django.contrib.auth.models import User

#serializer do usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')



# resgistrar o serializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id', 'username', 'email', 'password')
        extra_kwargs = { 'password': {'write_only': True}}

    def create(self, validated_data):
        # verifica se senha e usuario e email e valido
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])


        return user

