from django.db import models

class DigitalProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Handles prices like 250.50
    digital_file = models.FileField(upload_to='secure_downloads/')  # Stores the product file
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
