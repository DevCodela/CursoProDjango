from django.contrib import admin
from .models import Event, Category, Assistant, Comments

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Assistant)
admin.site.register(Comments)