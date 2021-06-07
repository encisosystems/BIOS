from cms.models import FooterDescription, Template


def get_footer_description_list_context_processor(request):
    templates = Template.objects.filter(is_active=True)
    if templates:
        template = templates.first()
        print(f'template={template}')
    else:
        template = Template.objects.create(is_active=True, header_title='Index')

    footer_sections = template.footerdescription_set.all()
    menu_items = template.menu_items.all()
    return {
        'footer_list': footer_sections,
        'template': template,
        'menu_items': menu_items
    }
