from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyMotoMadness.messagebox'

    def ready(self):
        import MyMotoMadness.messagebox.signals
        result = super().ready()
        return result