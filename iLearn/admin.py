from django.contrib import admin
from .models import Word

# Register your models here.
class wordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')

admin.site.register(Word,wordAdmin)
    