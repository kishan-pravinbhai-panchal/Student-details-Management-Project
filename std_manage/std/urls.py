from django.urls import path
from .views import *
urlpatterns = [
    path("",Home),
    path("home/",Home),
    path("add-std/",std_add),
    path("delete-std/<int:roll>",delete_std),
    path("update-std/<int:roll>",update_std),
    path("do-update-std/<int:roll>",do_update_std),
]