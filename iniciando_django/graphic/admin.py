from django.contrib import admin
from .models import Bomba, Motor, Curva, PontoCurva, Acoplamento

# Register your models here.
admin.site.register(Bomba)
admin.site.register(Motor)
admin.site.register(Curva)
admin.site.register(PontoCurva)
admin.site.register(Acoplamento)
