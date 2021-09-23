from django.contrib import admin

# Register your models here.
from home.models import EditEdu,EditExp,EditProj,EditLin,EditSkill

admin.site.register(EditEdu)
admin.site.register(EditExp)
admin.site.register(EditProj)
admin.site.register(EditLin)
admin.site.register(EditSkill)

