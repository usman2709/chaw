# Generated by Django 4.0.6 on 2022-09-09 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_alter_shopcart_options_shopcart_cart_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(editable=False, max_length=50)),
                ('last_name', models.CharField(editable=False, max_length=50)),
                ('total', models.IntegerField(editable=False)),
                ('cart_code', models.CharField(editable=False, max_length=255)),
                ('pay_code', models.CharField(editable=False, max_length=36)),
                ('paid', models.BooleanField(default=False, editable=False)),
                ('pay_date', models.DateTimeField(auto_now_add=True)),
                ('admin_note', models.CharField(max_length=255)),
                ('admin_update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
                'managed': True,
            },
        ),
    ]
