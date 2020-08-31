from django.views.generic import TemplateView,ListView, FormView
from .models import List
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.shortcuts import redirect # Add this
# Create your views here.
class HomePageView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContactForm
    def form_valid(self, form):
	    message = "{name} / {email} said: ".format(
			name=form.cleaned_data.get('name'),
			email=form.cleaned_data.get('email'))
	    message+= "\n\n{0}".format(form.cleaned_data.get('message'))
	    try:
	    	send_mail(
	        subject=form.cleaned_data.get('subject'),
	        message=message,
	        from_email=form.cleaned_data.get('email'),
	        recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
	    )
	    except Exception as e:
	    	print(e)

	    return redirect('/')



class ListPageView(ListView):
	model = List
	template_name = 'list.html'



