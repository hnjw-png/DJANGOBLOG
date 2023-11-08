# Generated by Django 3.2.19 on 2023-11-08 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.DateField()),
                ('service', models.CharField(choices=[('w', 'wedding'), ('e', 'exam'), ('b', 'birthday'), ('w', 'work'), ('u', 'undecided')], default='undecided', max_length=50)),
                ('time', models.CharField(choices=[('2pm', '3pm'), ('4pm', '5pm'), ('6pm', '7pm')], default='3pm', max_length=15)),
                ('HowMany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.client')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='client',
            name='Reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.reservation'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
