# Generated by Django 4.2.1 on 2023-06-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('discription', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('ML', 'Milk'), ('AR', 'Animal RubberMat'), ('P', 'Pesticides'), ('TI', 'Tools & Instruments'), ('FA', 'Farm Accessories'), ('CR', 'Curd'), ('GP', 'Growth Promoters'), ('GH', 'Ghee'), ('PN', 'Plant Nutrients'), ('FC', 'Field Crops'), ('CS', 'Chilli Seeds')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
