from dataclasses import fields
from rest_framework import serializers
from testapp.models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'