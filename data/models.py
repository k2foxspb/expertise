from django.db import models


class Data(models.Model):
    A = models.CharField(max_length=255, blank=True, null=True)
    B = models.CharField(max_length=255, blank=True, null=True)
    C = models.CharField(max_length=255, blank=True, null=True)
    D = models.CharField(max_length=255, blank=True, null=True)
    E = models.CharField(max_length=255, blank=True, null=True)
    F = models.CharField(max_length=255, blank=True, null=True)
    G = models.CharField(max_length=255, blank=True, null=True)
    H = models.CharField(max_length=255, blank=True, null=True)
    I = models.CharField(max_length=255, blank=True, null=True)
    J = models.CharField(max_length=255, blank=True, null=True)
    K = models.CharField(max_length=255, blank=True, null=True)
    L = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, editable=False)

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = "строка в таблице"
        verbose_name_plural = "строки в таблице"
        ordering = ("-pk",)
