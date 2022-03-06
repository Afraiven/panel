from django.shortcuts import render
from api.models import Moods, ActualMood


def main(request):
    moods = Moods.objects.all()
    print(request)
    actmood = ActualMood.objects.first()
    context = {'moods': moods, 'actmood': actmood}
    return render(request, 'base.html', context)