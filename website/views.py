from django.conf import settings
from django.core.mail import send_mail
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
            contact = serializer.save()
            self._send_notification(contact)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _send_notification(self, contact):
        try:
            subject = f"New Inquiry from {contact.name} - {contact.get_inquiry_type_display()}"
            body = (
                f"Name: {contact.name}\n"
                f"Company: {contact.company or "N/A"}\n"
                f"Email: {contact.email}\n"
                f"Phone: {contact.phone or "N/A"}\n"
                f"Type: {contact.get_inquiry_type_display()}\n"
                f"Message:\n{contact.message}\n"
            )
            notify_email = getattr(settings, "NOTIFICATION_EMAIL", "szchijie@gmail.com")
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[notify_email],
                fail_silently=True,
            )
        except Exception:
            pass
