# Generated by Django 3.0.4 on 2020-03-23 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200323_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergym',
            old_name='cardName',
            new_name='card_name',
        ),
        migrations.RenameField(
            model_name='usergym',
            old_name='cardNumber',
            new_name='card_number',
        ),
        migrations.RenameField(
            model_name='usergym',
            old_name='medicdescription',
            new_name='medic_description',
        ),
        migrations.RenameField(
            model_name='usergym',
            old_name='typePlan',
            new_name='type_plan',
        ),
        migrations.RemoveField(
            model_name='usergym',
            name='birthday',
        ),
    ]