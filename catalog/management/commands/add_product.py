from django.core.management.base import BaseCommand
from django.template.context_processors import media

from catalog.models import Product, Category


class Command(BaseCommand):
    help = "add new products to the database"

    def handle(self, *args, **options):
        # Удаление старых данных
        def handle(self, *args, **kwargs):
            Category.objects.all().delete()
            Product.objects.all().delete()

        сategory_obj = Category.objects.create(
            category_name="Бытовые товары", description="Бытовые товары"
        )

        products = [
            {
                "product_name": "Тарелка",
                "description": "Фарфор",
                "category": сategory_obj,
                "price": "500",
                "created_at": "2025-02-05",
                "updated_at": "2025-02-05",
            },
            {
                "product_name": "Ложка",
                "description": "алюминиевая ",
                "category": сategory_obj,
                "price": "100",
                "created_at": "2025-02-05",
                "updated_at": "2025-02-05",
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"product: {product.product_name} added")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"product: {product.product_name} exist")
                )
