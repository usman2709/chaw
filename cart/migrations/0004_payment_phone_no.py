# Generated by Django 4.0.6 on 2022-09-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
