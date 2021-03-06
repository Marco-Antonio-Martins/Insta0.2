# Generated by Django 4.0.3 on 2022-05-07 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=150, verbose_name='Descrição')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(upload_to='')),
                ('arroba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]
