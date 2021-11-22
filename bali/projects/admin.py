from django.contrib import admin

from projects.models import (
    Project,
    Category,
    AdvantagesProject,
    Location,
    LocationFact,
    ProjectGallery,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


class LocationFactInline(admin.TabularInline):
    model = LocationFact


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [
        LocationFactInline,
    ]


class AdvantagesProjectInline(admin.TabularInline):
    model = AdvantagesProject


class GalleryInline(admin.TabularInline):
    fk_name = 'project'
    model = ProjectGallery


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_display_links = ('name', 'price')
    ordering = ('-date_added', )
    inlines = [
        GalleryInline,
        AdvantagesProjectInline,
    ]
