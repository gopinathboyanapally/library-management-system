from django.contrib import admin

from .models import Dj_Bookrelation
from .models import Dj_Book_issued

admin.site.register(Dj_Bookrelation)
admin.site.register(Dj_Book_issued)
