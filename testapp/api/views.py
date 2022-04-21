from ssl import DER_cert_to_PEM_cert
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.models import TestModel
from . serializers import TestSerializer
from rest_framework import status


class Listvue(APIView):
    def get(self, request, **kwargs):
        test = TestModel.objects.all()
        test2 = TestSerializer(test, many=True)
        return Response(test2.data)

    def post(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)