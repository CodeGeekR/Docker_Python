# Generated by Django 4.2.1 on 2023-06-15 16:02

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='producto',
            name='caracteristicas',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[shop.models.validate_image_resolution]),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[shop.models.validate_image_resolution]),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[shop.models.validate_image_resolution]),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_oferta',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
