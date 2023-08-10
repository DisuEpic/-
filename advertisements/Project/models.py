from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=100, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    class Meta:
        db_table = "advertisements"