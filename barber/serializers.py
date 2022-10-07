from rest_framework.serializers import ModelSerializer
from .models import Barber


class BarberSerializer(ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'
