# Generated by Django 4.2.7 on 2023-11-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
                ('age', models.FloatField(verbose_name='age')),
                ('gender', models.FloatField(verbose_name='gender')),
                ('height', models.FloatField(verbose_name='height')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('ap_hi', models.FloatField(verbose_name='ap_hi')),
                ('ap_lo', models.FloatField(verbose_name='ap_lo')),
                ('cholesterol', models.FloatField(verbose_name='cholesterol')),
                ('gluc', models.FloatField(verbose_name='gluc')),
                ('smoke', models.FloatField(verbose_name='smoke')),
                ('alco', models.FloatField(verbose_name='alco')),
                ('active', models.FloatField(verbose_name='active')),
                ('cardio', models.FloatField(verbose_name='cardio')),
                ('bp_category', models.FloatField(verbose_name='bp_category')),
            ],
        ),
    ]
