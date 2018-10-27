from django.contrib import admin
from incidentsprediction.models import *

# Register your models here.
admin.site.register(Value)
admin.site.register(Parameter)
admin.site.register(PredictModel)
admin.site.register(Systemofsystem)
admin.site.register(System)
admin.site.register(ApplicationSystem)
admin.site.register(Vsystemofsystem)
admin.site.register(Vsystem)
admin.site.register(Vapplicationsystem)
admin.site.register(InputParameter)
admin.site.register(OutputParameter)
admin.site.register(RelInputParameter)