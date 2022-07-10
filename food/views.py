from logging import getLogger


from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch

from .serializers import FoodListSerializer
from .models import FoodCategory, Food


logger = getLogger('foods')


class FoodViewSet(ModelViewSet):
    http_method_names = ('get',)
    serializer_class = FoodListSerializer

    def get_queryset(self):
        food_categories = FoodCategory.objects.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True)))
        return food_categories.filter(food__is_publish=True)
