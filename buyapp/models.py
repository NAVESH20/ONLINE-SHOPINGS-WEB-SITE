from django.db import models

class product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    Qty=models.IntegerField()
    image=models.ImageField(upload_to="image/")
