from rest_framework.routers import DefaultRouter

from .views import FoodViewSet


router = DefaultRouter()
router.register('foods', FoodViewSet, basename='food')
urlpatterns = router.urls
