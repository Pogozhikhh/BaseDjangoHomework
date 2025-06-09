from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'add new products to the database'

    def handle(self, *args, **options):
        category1, _ = Category.objects.get_or_create(category_name='товары для дома',
                                                      discription='бытовые товары')

        products = [
            {'product_name': 'Тарелка', 'description': 'Фарфор',
             'category': category1, 'price': '500',
             'created_at': '2025-02-05', 'updated_at': '2025-02-05'},
            {'product_name': 'Ложка', 'description': 'алюминиевая ',
             'category': category1, 'price': '100',
             'created_at': '2025-02-05', 'updated_at': '2025-02-05'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'product: {product.product_name} added'))
            else:
                self.stdout.write(self.style.WARNING(
                    f'product: {product.product_name} exist'))