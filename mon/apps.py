from django.apps import AppConfig


class MonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mon'

    def ready(self):
        from jobs.scheduler import start
        start()