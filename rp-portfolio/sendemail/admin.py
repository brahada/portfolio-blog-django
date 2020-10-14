from django.contrib import admin
from django import forms
from sendemail.models import Contact
# Register your models here.
from django.db.models import Q
class InputFilter(admin.SimpleListFilter):
    template = 'input_filter.html'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        types = qs.values_list('name')
        return list(types)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice
class titleFilter(InputFilter):
    parameter_name = 'name'
    title ='Name'
    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(name__icontains=bit)
            )
        return queryset.filter(any_name)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    list_filter = (titleFilter,)
    search=('subject',)
    date_hierarchy = 'date'

admin.site.register(Contact, ContactAdmin)
