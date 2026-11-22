from django.conf import settings
from django.utils.functional import SimpleLazyObject


def _has_index():
    from .models import IndexTerm
    return IndexTerm.objects.exists()


def biblio_site(request):
    """settings.BIBLIO_SITE, as "biblio", in every template; and
    has_index, so the menus link to the index only once it has terms
    (checked only when a template asks)."""
    return {"biblio": settings.BIBLIO_SITE,
            "has_index": SimpleLazyObject(_has_index)}
