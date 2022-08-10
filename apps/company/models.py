from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	pass

# create portfolio section
class Portfolio(models.Model):
	class Meta:
		verbose_name = "Porfolio"
		verbose_name_plural = "My Porfolio"

	portfolio_image = models.ImageField()
	portfolio_heading = models.CharField(max_length=100)
	portfolio_subheading = models.CharField(max_length=100)

	def __str__(self):
		return self.portfolio_heading
