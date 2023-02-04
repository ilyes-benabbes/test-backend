# Generated by Django 4.1.4 on 2022-12-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('localisation', models.CharField(max_length=60)),
                ('prix', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=200, null=True)),
                ('categorie', models.CharField(max_length=60, null=True)),
                ('img', models.ImageField(default='default.png', upload_to='images/')),
            ],
        ),
    ]