# Generated by Django 3.2.6 on 2021-08-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]