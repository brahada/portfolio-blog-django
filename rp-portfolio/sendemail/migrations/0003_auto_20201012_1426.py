# Generated by Django 3.1.2 on 2020-10-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0002_auto_20201009_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('d', 'Deals'), ('j', 'Jobs')], default='j', max_length=1),
            preserve_default=False,
        ),
    ]
