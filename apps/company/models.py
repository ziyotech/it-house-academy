from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	pass

# create portfolio section
class Portfolio(models.Model):
	class Meta:
		verbose_name = "Porfolio"
		verbose_name_plural = "My Porfolio"

	portfolio_image = models.ImageField(upload_to="portfolio")
	portfolio_heading = models.CharField(max_length=100)
	portfolio_subheading = models.CharField(max_length=100)

	def __str__(self):
		return self.portfolio_heading

# courses category
class Category_courses(models.Model):

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


# create contact us model
class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Apply"

    full_name = models.CharField(max_length=100)
    own_phone = models.IntegerField(default=998)
    extra_phone = models.IntegerField(default=998)
    message = models.CharField(max_length=120)
    category = models.ForeignKey(Category_courses, null=True, default=None, on_delete=models.CASCADE, related_name="category_contact")

    def __str__(self):
        return self.full_name
