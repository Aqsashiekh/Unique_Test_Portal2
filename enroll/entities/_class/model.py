from django.db import models


#  create class model
class class_model(models.Model):
    # id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)