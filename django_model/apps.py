from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_model'
    # this will affect in django admin panel verbose_name
    verbose_name = _("Django Models")
