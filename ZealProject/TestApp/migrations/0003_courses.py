# Generated by Django 5.1.5 on 2025-02-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='fallback.png', upload_to='')),
            ],
        ),
    ]
