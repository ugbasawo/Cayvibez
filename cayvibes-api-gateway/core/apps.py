from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
<<<<<<< HEAD

    # def ready(self) -> None:
    #     from .consumer import channel
    #     channel.start_consuming()
    #     channel.close()
    #     return super().ready()
=======
>>>>>>> d0568b6 (adding files)
