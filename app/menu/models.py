from django.db import models
from app.models import MenuBaseModel


class Menu(MenuBaseModel):
    show_on_main = models.BooleanField(verbose_name='показывать на главной')


class MenuItem(MenuBaseModel):
    url = models.URLField(verbose_name='ссылка на подпункт меню')
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='головное меню',
        related_name='menu_item',
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='родитель',
        related_name='children',
    )
