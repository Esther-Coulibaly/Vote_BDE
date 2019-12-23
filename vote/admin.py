from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Coin admin'
admin.site.site_title = 'espace admin'
admin.site.index_title = 'Bienvenue dans le coin des administrateurs'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ["question_text"]}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
