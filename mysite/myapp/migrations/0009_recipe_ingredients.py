# Generated by Django 2.1.7 on 2019-05-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190515_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]