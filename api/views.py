from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from api.models import *
from api.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.



class User(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,  status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Snippets(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer
    # lookup_field = 'id'
    def list(self,request,*args,**kwargs):
        result = self.serializer_class(self.queryset,many=True,context={'request':request}).data
        count = self.queryset.count()
        output = dict()
        output['result'] = result
        output['total_items'] = count
        # result['total_count'] = count
        return Response(output)

    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Tag(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # lookup_field = 'id'
    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,request)
        return Response(serializer.data)


class SnippetsDetail(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)

        serializers = SnippetsSerializer(snippet)
        return Response(serializers.data)

    def put(self, request, pk):
        snippet = Snippet.objects.get(pk=pk)
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet=Snippet.objects.get(pk=pk)
        snippet.delete()
        snippet = Snippet.objects.all()
        serializer = SnippetsSerializer(snippet, many=True, context={'request': request})
        return Response(serializer.data)
