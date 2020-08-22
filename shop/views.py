from django.views.generic import TemplateView,ListView
from .models import List

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

class ListPageView(ListView):
	model = List
	template_name = 'list.html'