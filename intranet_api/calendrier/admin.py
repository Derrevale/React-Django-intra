# Importation de l'interface d'administration de Django
from django.contrib import admin

# Importation de vos modèles de calendrier
from .models import Calendar, Event


# Enregistrement de la classe CalendarAdmin pour l'interface d'administration de Django
@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    # Définition des champs qui seront affichés dans la liste des calendriers dans l'interface d'administration de Django
    list_display = ('name',)
    # Définition des champs qui seront préremplis à partir de champs existants lors de la création d'un nouveau calendrier dans l'interface d'administration de Django
    prepopulated_fields = {'slug': ('name',)}


# Enregistrement de la classe EventTypeAdmin pour l'interface d'administration de Django
@admin.register(Event)
class EventTypeAdmin(admin.ModelAdmin):
    # Définition des champs qui seront affichés dans la liste des types d'événements dans l'interface d'administration de Django
    list_display = ('title',)
    # Définition des champs qui seront préremplis à partir de champs existants lors de la création d'un nouveau type d'événement dans l'interface d'administration de Django
    exclude = ('rrule',)


