from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Отметье, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html(
                "<span style='color: rgb(50, 205, 50); font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M")
    
    @admin.display
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M")
            return format_html(
                "<span style='color: rgb(253, 233, 16); font-weight: bold'>Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M")

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"