# Generated by Django 4.0.6 on 2022-09-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_payment_address_payment_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='c_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='address',
            field=models.CharField(default='a', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='city',
            field=models.CharField(default='a', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='phone_no',
            field=models.CharField(default='a', max_length=50),
        ),
    ]