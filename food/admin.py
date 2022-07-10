from django.contrib import admin


from .models import FoodCategory, Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    pass
