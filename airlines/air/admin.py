from django.contrib import admin
from .models import User, AddPlane, ConfirmTicket

admin.site.register(User)
admin.site.register(AddPlane)
admin.site.register(ConfirmTicket)
