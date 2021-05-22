# Generated by Django 3.1.1 on 2021-05-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='FooterDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('type_desc', models.CharField(blank=True, max_length=60, null=True)),
                ('value', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('alt', models.CharField(max_length=60)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='footer',
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
    ]
