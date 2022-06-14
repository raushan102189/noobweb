from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=10)
    additonal_number = models.IntegerField()
    # fav = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# a = User(name="John", email="raj@gmail.com", number=123456789,gender="male",additonal_number=21232)
# a.save()


  