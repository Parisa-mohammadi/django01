# Generated by Django 4.2.7 on 2024-06-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
