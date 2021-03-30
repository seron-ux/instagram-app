from django.apps import AppConfig


class NewConfig(AppConfig):
    name = 'new'
    def ready(self):
        import new.signals
