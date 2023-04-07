from django.contrib import admin
from .models import posts, cricket


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_index', 'title', 'created_on', 'status')

    def get_index(self, obj):
        return obj.id

    get_index.short_description = 'Index'


admin.site.register(posts, PostAdmin)
admin.site.register(cricket)
