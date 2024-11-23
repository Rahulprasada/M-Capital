from django.contrib import admin
from .models import stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content', 'url')  # This shows the fields in the list view
    search_fields = ('heading', 'content')  # Optional: allows searching by title or description

admin.site.register(stock, StockAdmin)
