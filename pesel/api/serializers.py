from rest_framework import serializers
from .models import Pesel, Moods, ActualMood


class PeselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesel
        fields = "__all__"

class MoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moods
        fields = "__all__"
        
class ActualMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActualMood
        fields = "__all__"
        
        