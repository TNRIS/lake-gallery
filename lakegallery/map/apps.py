from django.apps import AppConfig


class MapConfig(AppConfig):
    name = 'map'

    def ready(self):
        import map.signals
