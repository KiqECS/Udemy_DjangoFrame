# Generated by Django 3.1.4 on 2020-12-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_centro', '0003_auto_20201222_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itens',
            name='id',
        ),
        migrations.AlterField(
            model_name='itens',
            name='code_item',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Código'),
        ),
    ]