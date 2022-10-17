from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Barber
from .serializers import BarberSerializer
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView

# Create your views here.

# Get all Barbers


class GetBarbers(ListView):
    template_name = "barber_list.html"
    model = Barber


# Get single Barber

class GetBarber(DetailView):
    model = Barber
    template_name = "single_barber.html"


# Update barber

class UpdateBarber(UpdateView):
    model = Barber
    fields = '__all__'

    template_name = "barber_update.html"


# Create a Barber
class CreateBarber(CreateView):
    model = Barber
    fields = '__all__'
    template_name = "create_barber.html"
