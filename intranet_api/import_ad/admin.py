from django.contrib import admin

from import_ad.models import SilvaUser


@admin.register(SilvaUser)
class SilvaUserAdmin(admin.ModelAdmin):
    """
    Administration view for SilvaUser entities.
    """

    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'site')
    list_filter = ('site',)
