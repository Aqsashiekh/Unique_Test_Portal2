from django.contrib import admin
from .models import User, objective_question, subjective_question, book, chapter
from enroll.entities._class.model import class_model

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'password','email','user_type', 'class_id', 'phone_number', 'address')

@admin.register(class_model)
class class_model(admin.ModelAdmin):
    list_display = ('id', 'class_name')

@admin.register(book)
class book(admin.ModelAdmin):
    list_display = ('book_name', 'class_id')

@admin.register(chapter)
class chapter(admin.ModelAdmin):
    list_display = ('book_id', 'chapter_name')

@admin.register(objective_question)
class objective_question(admin.ModelAdmin):
    list_display = ('question', 'option1', 'option2', 'option3', 'option4','right_option','chapter_id', 'time')

@admin.register(subjective_question)
class subjective_question(admin.ModelAdmin):
    list_display = ('question_statement', 'total_marks' , 'chapter_id')