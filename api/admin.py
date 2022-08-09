from django.contrib import admin
from .models import Scientific,ChoiceScientific,Literary,ChoiceLiterary
# Register your models here.
admin.site.register(Scientific)
admin.site.register(ChoiceScientific)

admin.site.register(Literary)
admin.site.register(ChoiceLiterary)