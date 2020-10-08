from django.contrib import admin
from .models import Category, Project, Career, Contact, Image, Tag, Ability, Video, Choose, Team, Instagram, Video_2, Achievements, Service

# Register your models here.

class ChooseAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_end', 'relevance']
    read_only = ['id', 'created']

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Career)
admin.site.register(Contact)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Ability)
admin.site.register(Video)
admin.site.register(Choose, ChooseAdmin)
admin.site.register(Team)
admin.site.register(Instagram)
admin.site.register(Video_2)
admin.site.register(Achievements)
admin.site.register(Service)











