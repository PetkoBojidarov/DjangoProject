from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CoockingWebsite.accounts'

    def ready(self):
        import CoockingWebsite.accounts.signals

