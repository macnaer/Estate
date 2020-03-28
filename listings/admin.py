from django.contrib import admin


from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', "tittle", "is_published",
                    "price", "list_date", "realtor")
    list_diaplay_links = ('id', "tittle")
    list_filter = ("realtor",)
    list_editable = ("is_published",)
    search_fields = ("tittle", "price", "description",
                     "address", "city", "state")
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
