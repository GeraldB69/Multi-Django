from django.contrib import admin

from todo_app.models import Task


@admin.register(Task)
class SimpleTaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    list_display = (
        'pk', 'title', 'description', 'closed', 'created_at', 'updated_at',
    )
    # list_editable = ('title',)
    list_display_links = ('title',)
    list_filter = ('closed',)
    search_fields = ['title', 'description', ]

# admin.site.register(Task, TaskAdmin)
