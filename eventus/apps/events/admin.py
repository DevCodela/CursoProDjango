from django.contrib import admin
from .models import Event, Category, Assistant, Comments

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name','category','start','finish','is_free','organizer',)

admin.site.register(Category)
admin.site.register(Assistant)
admin.site.register(Comments)