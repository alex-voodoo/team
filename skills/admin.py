from django.contrib import admin
from skills.models import Category, Skill, Measurement, PersonAssessment

admin.site.register(PersonAssessment)
admin.site.register(Measurement)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category',)
    ordering = ('category__name', 'name')
