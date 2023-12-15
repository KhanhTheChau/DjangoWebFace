from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users" # tên của ứng dụng được sử dụng trong cấu hình Django và URL patterns.
    
    def ready(self):
        import users.signals    
