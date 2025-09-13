from django.contrib import admin
from .models import Category, Tag, ScreenshotGroup, Screenshot
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_per_page = 50


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_per_page = 50


@admin.register(ScreenshotGroup)
class ScreenshotGroupAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "created_at")
    search_fields = ("title",)
    list_per_page = 50


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ("category", "format_image", "resolution", "order")
    list_per_page = 50

    def format_image(self, obj):
        if obj.image:
            return format_html(
                "<a href='{}'><img src='{}' width='200'></a>",
                obj.image.url,
                obj.image.url,
            )

    def resolution(self, obj):
        return f"{obj.width}x{obj.height}" if obj.width and obj.height else "N/A"

    format_image.short_description = "画像"
