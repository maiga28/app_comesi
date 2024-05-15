# your_app_name/apps.py

from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'main_apps'

    def ready(self):
        from . import signals  # Importer le module de signaux
