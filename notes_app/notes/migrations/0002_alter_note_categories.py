# Generated by Django 5.0.3 on 2024-03-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='categories',
            field=models.ManyToManyField(related_name='notes', to='notes.category'),
        ),
    ]
