from django.urls import path

from menu.views import IndexView

urlpatterns = [path('', IndexView.as_view())]
