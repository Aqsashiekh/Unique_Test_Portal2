# Generated by Django 3.2.13 on 2022-06-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('class_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField()),
                ('chapter_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='objective_question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.IntegerField()),
                ('option1', models.IntegerField()),
                ('option2', models.IntegerField()),
                ('option3', models.IntegerField()),
                ('option4', models.IntegerField()),
                ('right_option', models.CharField(max_length=100)),
                ('chapter_id', models.IntegerField()),
                ('time', models.DateTimeField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='class_model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subjective_question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_statement', models.CharField(max_length=100)),
                ('total_marks', models.IntegerField()),
                ('chapter_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('user_type', models.CharField(max_length=70)),
                ('class_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=70)),
            ],
        ),
    ]
