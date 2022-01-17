from django.contrib import admin

from .models import Event
from .models import CSEvent
from .models import ITEvent
from .models import EXTCEvent
from .models import INSTRUEvent
from .models import KEvent
from .models import SEvent
from .models import AEvent
from .models import GEvent

admin.site.site_header = 'RAIT CALENDAR ADMIN PANEL'



admin.site.register(Event)
admin.site.register(CSEvent)
admin.site.register(ITEvent)
admin.site.register(EXTCEvent)
admin.site.register(INSTRUEvent)
admin.site.register(KEvent)
admin.site.register(SEvent)
admin.site.register(AEvent)
admin.site.register(GEvent)