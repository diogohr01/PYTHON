from django.apps import AppConfig


class AppLivrariaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_livraria'


class LivroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livro'