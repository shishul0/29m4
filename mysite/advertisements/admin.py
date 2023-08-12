from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'updated_date', 'created_date', 'auction']
    list_filter = ['created_at', 'auction']
    actions = ["mark_auction_as_true", "mark_auction_as_false"]
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description'),
            'classes': ['collapse']
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )
    search_fields = ['title', 'price']

    @admin.action(description="аукциону быть")
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description="аукциону не быть")
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)