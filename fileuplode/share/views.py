from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from share.serializers import FileListSerializer, FileSerializer


class HandlefileUplode(APIView):
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'file uploded successfully'
                })
            return Response({
                'status': 400,
                'message': 'somthing went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
