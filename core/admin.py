from django.contrib import admin
from .models import Project, ContactMessage, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'status', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

admin.site.register(ContactMessage)