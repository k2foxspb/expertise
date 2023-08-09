from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from exp.models import News
from services.models import Services


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ServicesSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return Services.objects.all()

    def lastmod(self, obj):
        return obj.updated


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"
    protocol = 'https'

    def items(self):
        return ["exp:about", "exp:employ", "exp:aboutWork"]

    def location(self, item):
        return reverse(item)
