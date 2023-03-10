# Generated by Django 4.1.2 on 2023-01-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cirrhosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.IntegerField()),
                ('ascites', models.IntegerField()),
                ('hepatomegaly', models.IntegerField()),
                ('spiders', models.IntegerField()),
                ('edema', models.IntegerField()),
                ('bilirubin', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('albumin', models.FloatField()),
                ('copper', models.FloatField()),
                ('alk_phos', models.FloatField()),
                ('sgot', models.FloatField()),
                ('triglycerides', models.FloatField()),
                ('platelets', models.FloatField()),
                ('prothrombin', models.FloatField()),
            ],
        ),
    ]
