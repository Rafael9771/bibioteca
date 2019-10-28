# Generated by Django 2.2.5 on 2019-10-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20191028_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='compraR',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.login')),
                ('revista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Revista')),
            ],
        ),
    ]
