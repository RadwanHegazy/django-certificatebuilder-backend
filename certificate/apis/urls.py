from django.urls import path
from .views import create

urlpatterns = [
    path('create/', create.create_cer_view.as_view(),name="CreateCertificate"),
]