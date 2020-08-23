from django.views.generic import TemplateView,ListView,FormView
from .models import List
from .forms import ContactForm
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(FormView):
	form_class = ContactForm
	template_name = 'index.html'
	success_url = '/'

class ListPageView(ListView):
	model = List
	template_name = 'list.html'
