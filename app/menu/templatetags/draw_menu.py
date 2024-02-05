from django import template
from django.db.models import QuerySet
from django.utils.datastructures import MultiValueDictKeyError

from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    """
    Возвращает словарь с данными для отображения древовидного меню.

    Parameters:
        context: Словарь контекста шаблона Django, содержащий информацию
            о текущем запросе.
        menu: Заголовок меню, для которого нужно отобразить элементы.

    Returns:
        dict: Словарь с данными для отображения меню.
    """
    items = MenuItem.objects.filter(menu__title=menu)
    items_values = items.values()
    root_items = [item for item in items_values.filter(parent=None)]
    try:
        selected_item = items.get(id=context['request'].GET[menu])
        expanded_items_id = get_expanded_items_id(selected_item)
        for parent in root_items:
            if parent['id'] in expanded_items_id:
                parent['children'] = get_child_items(
                    items_values, parent['id'], expanded_items_id
                )
    except MultiValueDictKeyError:
        pass
    return {'items': root_items, 'menu': menu}


def get_expanded_items_id(parent: MenuItem) -> list[MenuItem]:
    """
    Возвращает список id развернутых пунктов меню, находящихся выше указанного.

    Parameters:
        parent: Родительский элемент меню.

    Returns:
        list: Список идентификаторов развернутых пунктов меню.
    """
    expanded_items = []
    while parent:
        expanded_items.append(parent.id)
        parent = parent.parent
    return expanded_items


def get_child_items(
    item_values: QuerySet[dict],
    current_parent_id: int,
    expanded_items_id: list[int],
):
    """
    Возвращает список дочерних элементов для указанного родительского элемента.

    Parameters:
        item_values: Значения элементов меню.
        current_parent_id: Идентификатор текущего родительского элемента меню.
        expanded_items_id: Список идентификаторов развернутых пунктов меню.

    Returns:
        list[int]: Список дочерних элементов для родительского элемента меню.

    """
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=current_parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in expanded_items_id:
            child['children'] = get_child_items(
                item_values, child['id'], expanded_items_id
            )
    return current_parent_child_list
