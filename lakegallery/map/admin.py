from django.contrib.gis import admin
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks, StoryContent


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')


class StoryContentAdmin(admin.ModelAdmin):
    list_display = ['lake']
    fieldsets = [
        (None,               {'fields': ['lake', 'summary', 'history']}),
        ('Additional Section 1', {'fields': ['section_one_nav',
                                             'section_one_header',
                                             'section_one_content',
                                             'section_one_photo',
                                             'image_tag']}),
        ('Additional Section 2', {'fields': ['section_two_nav',
                                             'section_two_header',
                                             'section_two_content']}),
        ('Additional Section 3', {'fields': ['section_three_nav',
                                             'section_three_header',
                                             'section_three_content']}),
    ]
    readonly_fields = ('image_tag',)

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
admin.site.register(StoryContent, StoryContentAdmin)
