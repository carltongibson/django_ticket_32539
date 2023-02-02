from django.contrib import admin

from .models import MyModel


class NrOfMembersFilter(admin.SimpleListFilter):
    title = "number of members"
    parameter_name = "nr_of_members_partition"
    access_filters_in_lookups = True

    def lookups(self, request, model_admin):
        changelist = model_admin.get_changelist_instance(request)
        filtered_qs = changelist.get_queryset(request)
        return [
            ("5", "0 - 5 (%d)" % filtered_qs.filter(nr_of_members__lte=5).count()),
            ("more", "more than 5 (%d)" % filtered_qs.filter(nr_of_members__gt=5).count()),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == "5":
            return queryset.filter(nr_of_members__lte=5)
        if value == "more":
            return queryset.filter(nr_of_members__gt=5)

class GenreFilter(admin.SimpleListFilter):
    title = "genre"
    parameter_name = "genre"
    access_filters_in_lookups = True

    def lookups(self, request, model_admin):
        changelist = model_admin.get_changelist_instance(request)
        filtered_qs = changelist.get_queryset(request)
        return [
            ("ROCK", "Rock (%d)" % filtered_qs.filter(genre="ROCK").count()),
            ("POP", "Pop (%d)" % filtered_qs.filter(genre="POP").count()),
            ("JAZZ", "Jazz (%d)" % filtered_qs.filter(genre="JAZZ").count()),
            ("CLASSICAL", "Classical (%d)" % filtered_qs.filter(genre="CLASSICAL").count()),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(genre=value)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "nr_of_members", "genre"]
    list_filter = [NrOfMembersFilter, GenreFilter]


admin.site.register(MyModel, MyModelAdmin)
