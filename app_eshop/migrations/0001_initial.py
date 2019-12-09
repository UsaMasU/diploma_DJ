# Generated by Django 2.0.5 on 2019-12-09 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10, verbose_name='Price')),
                ('qty', models.CharField(max_length=10, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Cultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=30, verbose_name='Symbol of...')),
                ('rarity', models.CharField(max_length=30, verbose_name='Rarity or exclusive')),
                ('description', models.TextField(max_length=255, verbose_name='Description text')),
            ],
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255, verbose_name='Description text')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, verbose_name='Model')),
                ('cpu', models.CharField(max_length=15, verbose_name='CPU type')),
                ('cpu_cores', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='CPU cores')),
                ('ram', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='RAM Gb')),
                ('int_flash', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Internal flash disk Gb')),
                ('ext_flash_type', models.CharField(max_length=30, verbose_name='External flash support')),
                ('ext_flash', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='External flash disk Gb')),
                ('cam', models.CharField(max_length=30, verbose_name='Cameras')),
                ('gsm_ranges', models.CharField(max_length=30, verbose_name='GSM work ranges')),
                ('internet', models.CharField(max_length=30, verbose_name='Mobile internet work range')),
                ('pay', models.CharField(max_length=30, verbose_name='Pay system support')),
                ('display_type', models.CharField(max_length=30, verbose_name='Display type')),
                ('display_size', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Display size (inch)')),
                ('nav', models.CharField(max_length=30, verbose_name='Navigation support')),
                ('os', models.CharField(max_length=30, verbose_name='OS version')),
                ('sim_type', models.CharField(max_length=30, verbose_name='SIM-card type')),
                ('sim_cards', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='SIM-cards quantity ')),
                ('accum_capacity', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Accumulator capacity')),
                ('body', models.CharField(max_length=30, verbose_name='Type of body')),
                ('color', models.CharField(max_length=30, verbose_name='Color')),
                ('dimensions', models.CharField(max_length=30, verbose_name='Dimensions')),
                ('weight', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Weight g')),
                ('description', models.TextField(max_length=255, verbose_name='Description text')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('price', models.CharField(max_length=10, verbose_name='Price')),
                ('qty', models.CharField(max_length=10, verbose_name='Quantity')),
                ('image', models.CharField(max_length=128, verbose_name='Image')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('status', models.CharField(choices=[('available', 'Available'), ('not available', 'Not available'), ('awaiting delivery', 'Awaiting delivery'), ('discontinued', 'Discontinued')], default='available', max_length=30)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Количество')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Cart', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name="Author's name")),
                ('text', models.TextField(max_length=255, verbose_name='Review text')),
                ('rating', models.CharField(choices=[('1', '★'), ('2', '★★'), ('3', '★★★'), ('4', '★★★★'), ('5', '★★★★★')], default='1', max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('template_name', models.CharField(choices=[('phone', 'Телефон'), ('cultural', 'Культура'), ('miscellaneous', 'Разный')], default='Разный', max_length=30)),
                ('location', models.CharField(choices=[('---', '---'), ('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right'), ('section 1', 'Section 1'), ('section 2', 'Section 2'), ('section 3', 'Section 3'), ('section 4', 'Section 4')], default='---', max_length=30)),
                ('slug', models.SlugField(default=0, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(through='app_eshop.ProductsInCart', to='app_eshop.Cart', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Section'),
        ),
        migrations.AddField(
            model_name='phone',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Product'),
        ),
        migrations.AddField(
            model_name='miscellaneous',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Product'),
        ),
        migrations.AddField(
            model_name='cultural',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Product'),
        ),
    ]
