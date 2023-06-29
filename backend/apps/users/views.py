from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User

from .serializers import *
from .services import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']
    my_tags = ['Users']

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = UserService().create(serializer.validated_data, request.user.id)
        return Response(UserSerializer(result).data,
                        status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs):
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = UserService().update(kwargs['pk'], serializer.validated_data, request.user.id)
        return Response(UserSerializer(result).data,
                        status=status.HTTP_200_OK)
        
    def destroy(self, request: Request, *args, **kwargs):
        UserService().destroy(kwargs['pk'], request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    @action(detail=False, pagination_class=None)
    def me(self, request: Request, *args, **kwargs):
        result = UserService().get_me(request.user.id)
        return Response(UserSerializer(result).data,
                        status=status.HTTP_200_OK)