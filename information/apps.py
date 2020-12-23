from django.apps import AppConfig


class InformationConfig(AppConfig):
    name = 'information'
    def ready(self):
        import information.signals