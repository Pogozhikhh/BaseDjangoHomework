from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserCreationsForm


class RegisterView(CreateView):
    template_name = "user/registration.html"
    form_class = UserCreationsForm
    success_url = reverse_lazy("catalog:products")

    def form_valid(self, form):
        user = form.save()

        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем Каталоге!"
        from_email = "pogozhikh.alexey@yandex.ru"
        recipient_list = [
            user_email,
        ]
        send_mail(subject, message, from_email, recipient_list)