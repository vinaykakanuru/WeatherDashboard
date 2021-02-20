from django.db import models

# Create your models here.


class City(models.Model):
    city_name = models.CharField(max_length=100, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'City'
        verbose_name = 'city'
