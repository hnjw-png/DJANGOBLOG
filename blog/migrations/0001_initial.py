# Generated by Django 3.2.19 on 2023-11-13 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='UPDATE', max_length=200)),
                ('description', models.TextField(default='its party time', max_length=200)),
                ('service', models.TextField(choices=[('w', 'wedding'), ('e', 'exam'), ('b', 'birthday'), ('w', 'work'), ('u', 'undecided')], default='undecided', max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[('2pm', '3pm'), ('4pm', '5pm'), ('6pm', '7pm')], default='3pm')),
                ('location', models.CharField(default='somewhere', max_length=200)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.reservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
