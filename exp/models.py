from pathlib import Path
from time import time

from django.db import models

from django.urls import reverse

from exp.services.utils import unique_slugify


def news_image_path(instance, filename):
    # file will be uploaded to
    #   MEDIA_ROOT / user_<username> / avatars / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f'news_{instance.title}/image/pic_{num}{suff}'


class News(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name="Title")
    preamble = models.CharField(max_length=1024, verbose_name="Preamble")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)
    slug = models.CharField(verbose_name='slug', max_length=255, blank=True, unique=True)
    image = models.ImageField(upload_to=news_image_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

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

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ("-created",)
