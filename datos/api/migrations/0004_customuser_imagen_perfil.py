# Generated by Django 5.1 on 2024-09-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_publication_nombre_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
