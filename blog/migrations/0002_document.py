# Generated by Django 3.2.2 on 2021-05-20 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('document', models.FileField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]