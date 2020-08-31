from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)


    def __str__(self):
    	return self.Email