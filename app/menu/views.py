from django.views.generic import TemplateView
from menu.models import Menu


class IndexView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(show_on_main=True)
        return context
