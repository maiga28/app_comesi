# Generated by Django 4.2.8 on 2024-06-19 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_livraisonproduct_livraison_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraisonproduct',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.order'),
            preserve_default=False,
        ),
    ]
