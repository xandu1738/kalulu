from django.contrib import admin
from .models import Question, Option

admin.site.site_header = "Kalulu Admin"
admin.site.site_title = "Kalulu Admin Area"
admin.site.index_title = "Welcome to the Kalulu admin Area"


class OptionInline(admin.TabularInline):
    model = Option
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [OptionInline]

# admin.site.register(Question)
# admin.site.register(Option)


admin.site.register(Question, QuestionAdmin)
