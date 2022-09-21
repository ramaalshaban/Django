from django.apps import AppConfig
# here we will import th signal function here

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users' 

    def ready(self):
        import users.signals