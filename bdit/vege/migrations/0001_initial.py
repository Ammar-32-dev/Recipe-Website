# Generated by Django 5.0.4 on 2024-07-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_image', models.ImageField(upload_to='images')),
                ('receipe_ingredients', models.TextField(max_length=100)),
            ],
        ),
    ]
