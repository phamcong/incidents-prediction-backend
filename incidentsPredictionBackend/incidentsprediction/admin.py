from django.contrib import admin
from incidentsprediction.models import *

# Register your models here.
admin.site.register(Value)
admin.site.register(Parameter)
admin.site.register(PredictModel)