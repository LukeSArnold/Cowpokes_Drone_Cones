# Generated by Django 4.1.7 on 2023-11-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_cones', '0002_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('flavor', models.CharField(max_length=100)),
                ('coneFlavor', models.CharField(max_length=100)),
                ('scoopCount', models.IntegerField()),
                ('stockAvailable', models.IntegerField()),
            ],
        ),
    ]
