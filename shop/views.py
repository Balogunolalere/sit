from django.views.generic import TemplateView,ListView
from django.core.mail import send_mail
from .models import List
from .forms import ContactForm
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'
	form_name = ContactForm()


class ListPageView(ListView):
	model = List
	template_name = 'list.html'




