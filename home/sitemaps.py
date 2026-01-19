from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['about', 'contact', 'index']
    

    def location(self, item):
        return reverse(item)