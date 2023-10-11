# Generated by Django 4.2.4 on 2023-08-18 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mob_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contacts_number', models.ManyToManyField(blank=True, to='auth_app.user')),
                ('spam_cell_numbers', models.ManyToManyField(blank=True, to='auth_app.user')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
