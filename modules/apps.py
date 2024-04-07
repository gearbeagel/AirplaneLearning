from django.apps import AppConfig


class ModulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules'

    def ready(self):
        from . import signals
