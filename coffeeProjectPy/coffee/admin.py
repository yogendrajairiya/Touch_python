from django.contrib import admin
from .models import CoffeeVariety, CoffeeReview, Store, CoffeeCertificate
# # Register your models here.
class CoffeeReviewInline(admin.TabularInline):
    model = CoffeeReview
    extra = 2

class CoffeeVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    search_fields = ('name', 'type')
    list_filter = ('type',)
    inlines = [CoffeeReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    filter_horizontal = ('coffee_varieties',)

class CoffeeCertificateAdmin(admin.ModelAdmin):
    list_display = ('coffee', 'certificate_number', 'issued_by', 'issue_date', 'expiration_date')
    search_fields = ('coffee__name', 'certificate_number', 'issued_by')
    
admin.site.register(CoffeeVariety, CoffeeVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CoffeeCertificate, CoffeeCertificateAdmin)
