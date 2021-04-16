# Generated by Django 3.1.7 on 2021-04-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_date',
            field=models.DateTimeField(editable=False),
        ),
    ]