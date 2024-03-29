from pathlib import Path
from time import time

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

from django.urls import reverse
from email_signals.models import EmailSignalMixin

from exp.services.utils import unique_slugify


def news_image_path(instance, filename):
    # file will be uploaded to
    #   MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f'news_{instance.title}/image/pic_{num}{suff}'


class News(EmailSignalMixin, models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name="Заголовок")
    preamble = models.CharField(max_length=1024, verbose_name="Преамбула")
    body = models.TextField(blank=True, null=True, verbose_name="Текст")
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    widget = CKEditorUploadingWidget()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Отредактировано", editable=False)
    deleted = models.BooleanField(default=False, verbose_name='Пометить как удалённую')
    slug = models.CharField(verbose_name='URL-адрес', max_length=255, blank=True, unique=True, editable=False)
    image = models.ImageField(upload_to=news_image_path, null=True, blank=True, verbose_name='Иконка')
    image1 = models.ImageField(upload_to=news_image_path, blank=True)
    image2 = models.ImageField(upload_to=news_image_path, blank=True)
    image3 = models.ImageField(upload_to=news_image_path, blank=True)
    keyword = models.CharField(max_length=255, blank=True, verbose_name='ключевые слова')

    def get_absolute_url(self):
        return reverse("exp:news_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

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

    def management_mailing_list(self):
        """Recipient list includes management."""
        return ['sudexper2023@mail.ru']

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ("-created",)


