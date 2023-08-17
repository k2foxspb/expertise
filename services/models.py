from pathlib import Path
from time import time

from django.db import models
from django.urls import reverse

from services.services.utils import unique_slugify


def services_image_path(instance, filename):
    # file will be uploaded to
    #   MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f'services_{instance.title}/image/pic_{num}{suff}'


class Services(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    body = models.TextField(blank=True, null=True, verbose_name="Текст")
    price = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновление", editable=False)
    deleted = models.BooleanField(default=False, verbose_name='пометить удалённым')
    slug = models.CharField(verbose_name='URL-адрес', max_length=255, blank=True, unique=True, editable=False)
    image = models.ImageField(upload_to=services_image_path, verbose_name='иконка')
    description = models.CharField(max_length=255, blank=True, verbose_name='краткое описание')
    keyword = models.CharField(max_length=255, blank=True, null=True, verbose_name='ключевые слова')

    def get_absolute_url(self):
        return reverse("services:services_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("created",)
        indexes = [models.Index(fields=['created', 'deleted'])]
