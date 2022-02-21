from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class ProductType(models.Model):
# 	media_type = models.CharField(max_length=200)
# 	name = models.CharField(max_length=200)

class Country(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class ProductType(models.Model):
	media_type 	= models.CharField(max_length=200)
	name 		= models.CharField(max_length=200)

	def __str__(self):
		return self.media_type + ' ' + self.name

class FollowersType(models.Model):
	product_type	= models.ForeignKey(ProductType, on_delete=models.CASCADE)
	name 			= models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Quantity(models.Model):
	count = models.IntegerField()

	def __str__(self):
		return self.count

class Product(models.Model):
	# followers_type 	= models.ForeignKey(FollowersType, on_delete=models.CASCADE)
	product_type	= models.ForeignKey(ProductType, on_delete=models.CASCADE)
	country	 		= models.ForeignKey(Country, on_delete=models.CASCADE)
	quantity		= models.ForeignKey(Quantity, on_delete=models.CASCADE)
	profile_url		= models.CharField(max_length=200)

	def __str__(self):
		return self.profile_url

class Review(models.Model):
	product_type	= models.ForeignKey(ProductType, on_delete=models.CASCADE)
	user	 		= models.ForeignKey(User, on_delete=models.CASCADE)
	score			= models.IntegerField()
	content 		= models.CharField(max_length=200)

	def __str__(self):
		return self.content
