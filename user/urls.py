from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user.views import RegisterView

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:products"), name="logout"),
    path("registration/", RegisterView.as_view(), name="registration"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
