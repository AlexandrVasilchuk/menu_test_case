from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """Базовая модель админки для моделей проекта"""

    empty_value_display = '-пусто-'
    list_display = ('id', 'title')
