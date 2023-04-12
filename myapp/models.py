from django.db import models
   
class User_Data(models.Model):
   username = models.CharField(max_length=150)
   email= models.EmailField(max_length=150)
   password= models.CharField(max_length=150)
   confirm_password= models.CharField(max_length=150)


class University(models.Model):
    name = models.CharField(max_length=100)
    impact_rank = models.IntegerField()
    openness_rank = models.IntegerField()
    global_rank = models.IntegerField()
