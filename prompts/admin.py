from django.contrib import admin
from .models import Program, Prompt


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_filter = ('name', )


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_filter = ('program__name', )
    list_display = ('name', 'private', 
              "show_hmi", "play_beep", "can_omit",
              "barge_in", "async", "_type",
              "modify_date", "program")
