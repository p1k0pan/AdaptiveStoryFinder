from django.apps import AppConfig


class WikihowAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wikihow_app'


class ArticleConfig(AppConfig):
    name = 'article'