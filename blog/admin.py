from django.contrib import admin
from .models import post, category
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'creted_date'
    empty_value_display = '-empty-'
    #fields = ('title',)
    list_display = ('title', 'status', 'counted_views')
admin.site.register(post, PostAdmin)
admin.site.register(category)
# Register your models here.
