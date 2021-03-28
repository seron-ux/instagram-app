from __future__ import unicode_literals

from django.apps import AppConfig


class InstagramConfig(AppConfig):
    name = 'Instagram'

    def ready(self):
        import Instagram.signals