from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MoodsSerializer, ActualMoodSerializer

from .models import Moods, ActualMood

@api_view(['GET'])
def apiPesel(request):
    api_urls = {
        'List':'/pesel-list/',
        'Create':'/pesel/',
        'Delete':'/pesel-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def peselList(request):
    moods = Moods.objects.all()
    serializer = MoodsSerializer(moods, many=True)
    return Response(serializer.data)

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

@api_view(['POST', 'GET'])
def peselCreate(request):
    actmood = ActualMood.objects.get(id=1)
    serializer = ActualMoodSerializer(instance=actmood, data=request.data)

    if serializer.is_valid():
        serializer.save()

        # string
        nazwa = list(request.data.values())[0]
        response = list(request.data.values())[1]

        template = render_to_string('api/email_template.html', {'name':nazwa, 'response': response})
        email = EmailMessage(
            'nowe',
            template,
            settings.EMAIL_HOST_USER,
            ['hololiveu99@gmail.com'],
        )

        email.fail_silently=False
        email.send()

        return Response(serializer.data)
    return Response(serializer.data)
