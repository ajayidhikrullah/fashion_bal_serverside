from django.contrib import admin
from .models import Fashion, Style, news_letters
# Register your models here.

admin.site.register(Fashion)
admin.site.register(Style)
admin.site.register(news_letters)
