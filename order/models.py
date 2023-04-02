from django.db import models

class LaundryItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='laundry_images/', blank=True, null=True)

    def _str_(self):
        return self.name