# Generated by Django 3.2.25 on 2024-06-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(upload_to='originals/')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='thumbs/')),
                ('big_thumb', models.ImageField(blank=True, null=True, upload_to='big_thumbs/')),
                ('big_1920', models.ImageField(blank=True, null=True, upload_to='big_1920/')),
                ('d2500', models.ImageField(blank=True, null=True, upload_to='d2500/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
