from django.contrib import admin

# Register your models here.
from .models import Address
from .models import Authorship
from .models import AdminEmail
from .models import Institution
from .models import Journal
from .models import Keyword
from .models import Person
from .models import Publication
from .models import Publisher
from .models import Site
from .models import Subject

admin.site.register(Address)
admin.site.register(AdminEmail)
admin.site.register(Institution)
admin.site.register(Journal)
admin.site.register(Keyword)
admin.site.register(Person)


class AuthorshipInline(admin.TabularInline):
    model = Authorship
    fields = ('person', 'position')
    extra = 1


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    inlines = [AuthorshipInline]


admin.site.register(Publisher)
admin.site.register(Site)
admin.site.register(Subject)
