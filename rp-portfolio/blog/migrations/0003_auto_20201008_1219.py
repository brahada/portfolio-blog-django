# Generated by Django 3.1.2 on 2020-10-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_viewer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='viewer',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('r', 'Review'), ('t', 'Trash')], default='d', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
