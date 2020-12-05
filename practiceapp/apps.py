from django.apps import AppConfig


class PracticeappConfig(AppConfig):
    name = 'practiceapp'

    def ready(self):
        import practiceapp.signals