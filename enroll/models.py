from django.db import models

# Create your models here.
#  create User model
class User(models.Model):
    # id = models.IntegerField( primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user_type = models.CharField(max_length=100) 
    class_id = models.IntegerField() 
    phone_number = models.IntegerField() 
    address = models.CharField(max_length=100)

#  create book model
class book(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    class_id = models.IntegerField() 
    
#  create chapter model
class chapter(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    chapter_name= models.CharField(max_length=70) 
    
#  create objective_question model
class objective_question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.IntegerField()
    option1= models.IntegerField() 
    option2= models.IntegerField() 
    option3= models.IntegerField() 
    option4= models.IntegerField()
    right_option = models.CharField(max_length=100)
    chapter_id = models.IntegerField() 
    time= models.DateTimeField(max_length=70)

#  create subjective_question model
class subjective_question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_statement = models.CharField(max_length=100)
    total_marks= models.IntegerField()
    chapter_id = models.IntegerField() 



