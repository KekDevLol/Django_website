# Generated by Django 4.1.7 on 2023-03-12 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmsslider',
            old_name='сms_text',
            new_name='cms_text',
        ),
    ]
