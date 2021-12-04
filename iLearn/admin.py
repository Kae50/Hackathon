from django.contrib import admin
from .models import Word,Number

# Register your models here.
class wordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')

admin.site.register(Word,wordAdmin)

class numberAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')

admin.site.register(Number,numberAdmin)
    