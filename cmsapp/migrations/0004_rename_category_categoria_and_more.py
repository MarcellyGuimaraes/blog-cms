# Generated by Django 4.1 on 2022-08-17 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0003_alter_post_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='category_id',
            new_name='categoria_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoria',
        ),
    ]
