import os
from io import BytesIO
from uuid import uuid4

from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField("カテゴリ", max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "カテゴリ"

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField("タグ", max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "タグ"

    def __str__(self) -> str:
        return self.name


def upload_to(instance, filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    filename = f"{uuid4()}{ext}"
    return f"images/Screenshot/{filename}"


def thumbnail_upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    filename = f"{base}_thumb{ext}"
    return f"images/Screenshot/{filename}"


class ScreenshotGroup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリ",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name="タグ", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Screenshot(models.Model):
    recipe_group = models.ForeignKey(
        ScreenshotGroup,
        related_name="images",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to=upload_to, height_field="height", width_field="width"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリ",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name="タグ", blank=True)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_to, null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return self.image.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            img_path = self.image.path
            base, ext = os.path.splitext(os.path.basename(img_path))
            ext = ext.lower()
            thumb_name = f"{base}_thumb{ext}"

            with Image.open(img_path) as img:
                img.thumbnail((600, 600))
                buffer = BytesIO()
                img.save(buffer, format=img.format, quality=70)
                buffer.seek(0)
                self.thumbnail.save(thumb_name, ContentFile(buffer.read()), save=False)
                super().save(update_fields=["thumbnail"])
