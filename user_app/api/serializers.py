from dataclasses import fields
from tkinter.ttk import Style
from xml.parsers.expat import model
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(Style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_keyword = {
            'password':{'write_only': True}
        }