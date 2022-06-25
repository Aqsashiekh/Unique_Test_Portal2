from django.db import models


#  create class model
class class_model(models.Model):
    class_name = models.CharField(max_length=100)