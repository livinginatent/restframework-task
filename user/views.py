from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView


from .models import User


# Create your views here.


# Get all Users
class GetUsers(ListView):
    template_name = "user_list.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Get single User

class GetUser(DetailView):
    model = User
    template_name = "single_user.html"


# Update user

class UpdateUser(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', 'mobile')
    template_name = "user_update.html"


# Create a User
class CreateUser(CreateView):
    model = User
    fields = '__all__'
    template_name = "create_user.html"
