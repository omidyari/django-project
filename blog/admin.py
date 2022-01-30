from django.contrib import admin
from .models import post
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'creted_date'
    empty_value_display = '-empty-'
    #fields = ('title',)
    list_display = ('title', 'status', 'counted_views')
admin.site.register(post, PostAdmin)
# Register your models here.
