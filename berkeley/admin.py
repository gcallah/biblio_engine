from django.contrib import admin

# Register your models here.
from .models import Institution
from .models import Keyword
from .models import Person
from .models import Publisher
from .models import Journal
from .models import Publication

admin.site.register(Institution)
admin.site.register(Keyword)
admin.site.register(Person)
admin.site.register(Publisher)
admin.site.register(Journal)
admin.site.register(Publication)
