# Generated by Django 2.2.5 on 2019-10-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_libro_sinopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='sinopsis',
            field=models.CharField(default='o', max_length=1000, verbose_name='sinopsis'),
        ),
    ]
