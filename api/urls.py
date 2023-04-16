from django.urls import path
from rest_framework import routers

from api import views

router = routers.SimpleRouter()
router.register("users", views.UserViewSet, basename="users"),

urlpatterns = router.urls
