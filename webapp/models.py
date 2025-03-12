from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Dj_Bookrelation(models.Model):
	Dj_Book_isbn = models.CharField(max_length = 9, primary_key = True)
	Dj_Book_name = models.CharField(max_length = 50)
	Dj_Author = models.CharField(max_length = 50)
	Dj_Publisher = models.CharField(max_length = 50)
	Dj_Donor = models.CharField(max_length = 50, null=True)
	Dj_is_issued = models.BooleanField(default = False)

class Dj_Book_issued(models.Model):
	Dj_user = models.ForeignKey(User, null=True)
	Dj_Book_isbn = models.ForeignKey(Dj_Bookrelation, default = True, primary_key = True)
	Dj_Book = models.CharField(max_length = 50)
	Dj_issued_on = models.DateField()
	Dj_due_date = models.DateField()