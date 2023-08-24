from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyMotoMadness.accounts'

    def ready(self):
        import MyMotoMadness.accounts.singals
        result = super().ready()
        return result