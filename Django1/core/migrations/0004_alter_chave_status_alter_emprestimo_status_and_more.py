# Generated by Django 4.2.5 on 2023-09-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_chave_status_emprestimo_status_servidor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
