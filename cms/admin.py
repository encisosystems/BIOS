from django.contrib import admin
from .models import *


class FooterDescriptionInline(admin.StackedInline):
    model = FooterDescription
    extra = 0


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('menu_items', )
    inlines = (FooterDescriptionInline, )
    fields = ('is_active', 'icon', 'logo', 'header_title', 'menu_items')
    list_display = ('__str__', 'icon', 'logo', 'is_active')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page')
    fields = ('name', 'page', )
    raw_id_fields = ('page', )

#
# @admin.register(FooterDescription)
# class FooterDescriptionAdmin(admin.ModelAdmin):
#     pass


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


@admin.register(Carrousel)
class CarrouselAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass


class ContentInline(admin.StackedInline):
    model = Content
    extra = 0
    raw_id_fields = ('carrousel', )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (ContentInline, )


# @admin.register(Content)
# class ContentAdmin(admin.ModelAdmin):
#     pass

