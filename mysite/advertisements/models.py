from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Отметье, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)