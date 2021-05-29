from cms.models import FooterDescription


def get_footer_description_list_context_processor(request):
    footer_description_list = FooterDescription.objects.all()
    return {
        'footer_list': footer_description_list
    }
