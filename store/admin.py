from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from store import models
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
"""Inline Models"""

# CategoryAdmin inlines


class SubCategoryInline(admin.StackedInline):
    model = models.SubCategory
    extra = 0
    fields = ["title", "category"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_categories",)
    search_fields = ["title"]
    fields = ['title']
    inlines = [SubCategoryInline]


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("item_category", "title", "price",)
    search_fields = ["item_category", "title", "unit"]
    fields = ["item_category", "rental_period", "title", "price", "unit", "image"]


@admin.register(models.RentalPeriod)
class RentalPeriodAdmin(admin.ModelAdmin):
    list_display = ("period", "price",)
    search_fields = ["period"]


@admin.register(models.Location)
class RentalPeriodAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]


admin.site.register(models.HDYFU)
admin.site.register(models.TimeSlots)
admin.site.register(models.ExtraWork)