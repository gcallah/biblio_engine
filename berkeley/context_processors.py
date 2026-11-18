from django.conf import settings


def biblio_site(request):
    """settings.BIBLIO_SITE, as "biblio", in every template."""
    return {"biblio": settings.BIBLIO_SITE}
