from django.contrib import admin

from base_app.models import (
    DataConsultation,
    FAQ,
    Project,
    Category,
    AdvantagesProject,
    Location,
    LocationFact,
    Quiz,
    ProjectGallery,
)


@admin.register(DataConsultation)
class DataConsultationAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date_submission')
    list_display_links = ('phone', )
    ordering = ('-date_submission', )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_phone',
                    'order_type', 'budget')
    list_display_links = ('client_name', 'client_phone',
                          'order_type', 'budget')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_display_links = ('question', 'answer')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(AdvantagesProject)
class AdvantagesProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    list_display_links = ('name', )


@admin.register(LocationFact)
class LocationFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_display_links = ('title', )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


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
    ]
