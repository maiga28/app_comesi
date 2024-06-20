# Generated by Django 4.2.8 on 2024-06-19 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_livraison'),
    ]

    operations = [
        migrations.CreateModel(
            name='LivraisonProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.livraison')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.product')),
            ],
        ),
        migrations.AddField(
            model_name='livraison',
            name='products',
            field=models.ManyToManyField(related_name='livraisons', through='gestion.LivraisonProduct', to='gestion.product'),
        ),
    ]