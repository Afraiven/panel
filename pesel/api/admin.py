from django.contrib import admin


from .models import ActualMood, Moods

class ActualMoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(ActualMood, ActualMoodAdmin)


class MoodsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Moods, MoodsAdmin)