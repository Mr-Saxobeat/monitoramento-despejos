# Generated by Django 3.1.7 on 2021-05-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despejos', '0002_despejo_ameaca_a_lideranca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despejo',
            old_name='motivo_despejo',
            new_name='motivo',
        ),
        migrations.RenameField(
            model_name='despejo',
            old_name='responsavel_despejo',
            new_name='responsavel',
        ),
        migrations.AddField(
            model_name='despejo',
            name='etnia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='etnia'),
        ),
    ]
