from django.conf import settings
from django.db import models


class MenuBaseModel(models.Model):
    """Абстрактная модель для меню."""

    title = models.CharField(
        max_length=settings.MAX_TITLE_LENGTH, verbose_name='название'
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
