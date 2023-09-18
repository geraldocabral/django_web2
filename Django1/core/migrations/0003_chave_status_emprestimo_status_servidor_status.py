# Generated by Django 4.2.5 on 2023-09-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_chave_status_remove_emprestimo_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chave',
            name='status',
            field=models.BooleanField(default=0, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='status',
            field=models.BooleanField(default=0, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servidor',
            name='status',
            field=models.BooleanField(default=0, verbose_name='Status'),
            preserve_default=False,
        ),
    ]