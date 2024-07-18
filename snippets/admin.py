from django.contrib import admin
from snippets.models import Snippet, Comment

# admin.site.register(Snippet)
# admin.site.register(Comment)

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    fields = ('title', 'code', 'description')


@admin.register(Comment)
class SnippetAdmin(admin.ModelAdmin):
    fields = ('text',)
    list_display = ('text', 'commented_by', 'commented_to', 'commented_at')
    search_fields = ('text', 'commented_by', 'commented_to', 'commented_at')
    list_filter = ('commented_by', 'commented_to', 'commented_at',)