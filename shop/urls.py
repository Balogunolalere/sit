from django.urls import path
from .views import HomePageView,ListPageView,Thanks


urlpatterns = [

	path('', HomePageView.as_view(), name='home'),
	path('packages/', ListPageView.as_view(), name='list'),
	path('thanks/', Thanks.as_view(), name='thanks')
]