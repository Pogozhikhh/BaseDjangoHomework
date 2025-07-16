from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from user.models import CustomUsers


class Command(BaseCommand):
    def handle(self, *args, **options):
        CustomUsers = get_user_model()
        user = CustomUsers.objects.create(
            email="pogozhikhh@yandex.ru",
            first_name="Alexey",
            last_name="Pogozhikh",
        )

        user.set_password("admin")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user with email {user.email}!"
            )
        )