from rest_framework.routers import DefaultRouter

from core.views import ProjectViewSet, UserViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("users", UserViewSet)

urlpatterns = []
urlpatterns += router.urls
