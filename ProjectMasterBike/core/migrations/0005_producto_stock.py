# Generated by Django 4.2.1 on 2023-07-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_usuario_rutusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad del producto en stock'),
        ),
    ]
