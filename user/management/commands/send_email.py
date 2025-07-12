from django.core.mail import send_mail

try:
    send_mail(
        'Тема теста',
        'Тестовое сообщение',
        'pogozhikh.alexey@yandex.ru',
        ['pogozhikh.alexey@yandex.ru'],
        fail_silently=False,
    )
    print("Письмо отправлено успешно")
except Exception as e:
    print(f"Ошибка при отправке: {e}")