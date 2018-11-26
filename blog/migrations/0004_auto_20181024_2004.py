# Generated by Django 2.1.2 on 2018-10-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181024_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='breed',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('RE', 'Rescatado'), ('AV', 'Disponible'), ('AD', 'Adoptado')], default='RE', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
