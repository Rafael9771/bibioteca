# Generated by Django 2.2.5 on 2019-09-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=80, verbose_name='Username')),
                ('password', models.CharField(max_length=80, verbose_name='Paswword')),
            ],
        ),
    ]