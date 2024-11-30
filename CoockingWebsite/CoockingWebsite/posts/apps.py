from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CoockingWebsite.posts'

    def ready(self):
        import CoockingWebsite.posts.signals
