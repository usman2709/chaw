# Generated by Django 4.0.6 on 2022-08-12 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techbro', '0010_showcase_showsub_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showcase',
            options={'managed': True, 'verbose_name': 'Showcase', 'verbose_name_plural': 'Showcase'},
        ),
        migrations.RenameField(
            model_name='showcase',
            old_name='showsub_name',
            new_name='show_txt',
        ),
        migrations.AlterModelTable(
            name='showcase',
            table='showcase',
        ),
    ]
