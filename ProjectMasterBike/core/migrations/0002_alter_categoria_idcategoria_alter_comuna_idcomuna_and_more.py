# Generated by Django 4.2.1 on 2023-07-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de categoria'),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='idComuna',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de comuna'),
        ),
        migrations.AlterField(
            model_name='listacompras',
            name='idListaCompras',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la lista de compras'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de producto'),
        ),
        migrations.AlterField(
            model_name='region',
            name='idRegion',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de categoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id de usuario'),
        ),
    ]
