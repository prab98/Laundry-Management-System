from django.db import models

class LaundryItem(models.Model):
    date = models.DateField()
    Topwear = models.IntegerField()
    bottomwear = models.IntegerField()
    woolen = models.IntegerField()
    Contact_Number = models.IntegerField()
    address = models.CharField(max_length=500)

    def _str_(self):
        return self.Contact_Number