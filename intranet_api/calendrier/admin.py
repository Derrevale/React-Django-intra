from django.contrib import admin
from .models import Calendar, Event


class EventInline(admin.TabularInline):
    model = Event
    extra = 0
    fields = ('title', 'Debut', 'Fin', 'description')
    show_change_link = True
    verbose_name_plural = 'Events'


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [EventInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'Debut', 'Fin', 'location')
    list_filter = ('category', 'recurrency')
    search_fields = ('title', 'location')
    exclude = ('rrule',)

    fieldsets = (
        (None, {
            'fields': ('title','category', 'Debut', 'Fin', 'location','description')
        }),
        ('Optional', {
            'fields': ('recurrency','frequency', 'count', 'interval'),
            'classes': ('collapse',)
        }),
    )
