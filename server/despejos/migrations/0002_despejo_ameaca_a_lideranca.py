# Generated by Django 3.1.7 on 2021-05-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despejos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despejo',
            name='ameaca_a_lideranca',
            field=models.TextField(blank=True, null=True, verbose_name='ameaça a liderança'),
        ),
    ]
