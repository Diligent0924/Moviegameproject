from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# 내부망
from .models import User


# Create your views here.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, user_name):
    user = get_object_or_404(User, username = user_name)
    print(user)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)