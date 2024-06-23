# Generated by Django 4.2.8 on 2024-06-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comionneur', '0005_alter_camionneur_options_alter_camionneur_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camionneur',
            options={'verbose_name': 'Camionneur', 'verbose_name_plural': 'Camionneurs'},
        ),
        migrations.AlterField(
            model_name='camionneur',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
