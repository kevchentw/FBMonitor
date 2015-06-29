from django.contrib import admin
from .models import FBData


class FBDataAdmin(admin.ModelAdmin):
        list_display = ('page_id', 'post_id', 'comments', 'likes', 'shares')

admin.site.register(FBData, FBDataAdmin)
