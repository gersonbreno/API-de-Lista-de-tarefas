# Generated by Django 5.0.6 on 2024-05-16 18:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('discricao', models.TextField()),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
