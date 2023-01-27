from django.contrib import admin
from . import models


@admin.action(description="Activate selected blogs")
def active_blogs(modelAdmin, request, queryset):
    queryset.update(active=1)


@admin.action(description='Deactivate selected blogs')
def deactivate_blogs(modeladmin, request, queryset):
    queryset.update(active=0)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


def date_posted(obj):
    return obj.date_posted.date()


class BlogAdmin(admin.ModelAdmin):
    actions = [active_blogs, deactivate_blogs]
    list_display = ('title', 'date_posted', 'active',)
    search_fields = ['title', 'content']
    list_filter = ('active',)
    prepopulated_fields = {'slug': ('title',)}


# Register models
admin.site.register(models.Blog)
admin.site.register(models.Category)
