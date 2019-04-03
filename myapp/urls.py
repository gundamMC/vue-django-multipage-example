from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="app"),
    path('new_page', TemplateView.as_view(template_name="new_page.html"), name="new_page")
]
