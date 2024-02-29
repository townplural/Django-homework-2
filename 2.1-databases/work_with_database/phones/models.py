from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    image = models.URLField(blank=True)
    price = models.CharField(max_length=50, blank=True)
    release_date = models.CharField(max_length=50, blank=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(name)
    pass
