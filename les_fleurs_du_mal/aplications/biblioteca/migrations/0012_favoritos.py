# Generated by Django 2.2.5 on 2019-10-30 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0011_remove_login_favoritos'),
    ]

    operations = [
        migrations.CreateModel(
            name='favoritos',
            fields=[
                ('id_favorito', models.AutoField(primary_key=True, serialize=False)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Libro')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.login')),
            ],
        ),
    ]