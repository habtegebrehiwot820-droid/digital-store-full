from django.db import models

class DigitalProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    supplier_name = models.CharField(max_length=100, blank=True, null=True, help_text="Where do you source this from?")
    reseller_link = models.URLField(blank=True, null=True, help_text="External affiliate or supplier checkout link")
    digital_file = models.FileField(upload_to='digital_files/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title