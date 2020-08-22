from django.db import models

# Create your models here.
class List(models.Model):
	List_Header = models.CharField(max_length=150)
	Item = models.CharField(max_length=100)
	Price = models.CharField(max_length=100)
	Quantity = models.IntegerField()


	class Meta:
	    verbose_name = "List"
	    verbose_name_plural = "Lists"

	def __str__(self):
	    return self.List_Header
    