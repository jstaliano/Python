# Generated by Django 3.0.5 on 2020-04-14 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200414_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='alug',
            new_name='slug',
        ),
    ]
