from django.apps import AppConfig


class DataManagerConfig(AppConfig):
    name = 'Data_Manager'

    def ready(self):
        import Data_Manager.signals