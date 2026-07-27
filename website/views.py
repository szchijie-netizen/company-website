from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ContactSerializer

class CompanyInfoView(APIView):
    def get(self, request):
        return Response({
            'name': 'Shenzhen Chijie International Trade Co., Ltd.',
            'description': 'Your Trusted Partner in Global Trade',
            'contact': {
                'address': 'A1813, Tang Shang Building, 35 Xinqiao Section, Guangshen Road, Shangxing Community, Xinqiao Street, Bao\'an District, Shenzhen',
                'phone': '+86 18631076789',
                'email': 'szchijie@gmail.com',
                'whatsapp': '+852 54654752',
                'hours': '24/7',
            }
        })


class ContactCreateView(APIView):
    """POST /api/contact/ — 前端提交留言"""

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
