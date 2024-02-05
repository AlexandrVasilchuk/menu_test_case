from django.contrib import admin
from menu.models import Menu, MenuItem
from app.admin import BaseAdmin


class MenuItemInline(admin.TabularInline):
    model = MenuItem


@admin.register(Menu)
class MenuAdmin(BaseAdmin):
    inlines = [MenuItemInline]
