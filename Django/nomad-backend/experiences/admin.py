from django.contrib import admin
from .models import Experience, Perk


# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start",
        "end",
        "created_at",
    )

    list_filter = ("categoryy",)


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
    )
