# Generated by Django 5.1.2 on 2024-11-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preparations',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='No description provided', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='preparation_time',
            field=models.CharField(default='No description provided', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='recipes_images',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images/'),
        ),
    ]
