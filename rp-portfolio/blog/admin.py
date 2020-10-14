from django.contrib import admin
from blog.models import Post, Category, Comment
from django.db.models import Q
class InputFilter(admin.SimpleListFilter):
    template = 'input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

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
    parameter_name = 'title'
    title ='Title'
    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(title__icontains=bit)
            )
        return queryset.filter(any_name)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "status",)
    list_filter=(titleFilter,)
    actions = ['delete_selected', 'publish_selected']

    def publish_selected(self, request, queryset):
        queryset.update(status='p')

    publish_selected.short_description = "Publish the selected posts"

    def get_actions(self, request):
        # Disable delete
        actions = super(PostAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

class CategoryAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    list_display=("post","body",)
    list_filter=("created_on",)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin )
