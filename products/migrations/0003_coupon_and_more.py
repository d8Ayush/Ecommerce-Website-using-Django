# Generated by Django 5.0.1 on 2024-06-11 19:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_product_color_variant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('coupon_code', models.CharField(max_length=20)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_amount', models.IntegerField(default=False)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_desription',
            new_name='product_description',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='colorvariant',
            name='color_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='size_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
