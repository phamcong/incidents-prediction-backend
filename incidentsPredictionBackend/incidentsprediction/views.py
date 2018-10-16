from django.shortcuts import render
from incidentsprediction.models import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from incidentsprediction.predictionmodels import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def predmodel_list(request):
    """
    List all models, or create a new models.
    """
    if request.method == 'GET':
        try:
            qmodels = PredictModel.objects.all()
            models = []
            for qmodel in qmodels:
                model = model_to_dict(qmodel)
                qparameters = qmodel.parameters.get_queryset()
                parameters = []
                for qparameter in qparameters:
                    parameter = model_to_dict(qparameter)
                    qvalues = qparameter.values.get_queryset()
                    parameter['values'] = [model_to_dict(qvalue) for qvalue in qvalues]
                    parameters.append(parameter)
                model['parameters'] = parameters
                print(model)
                models.append(model)
            return JsonResponse({ 'models': models })
        except Exception as e:
            return HttpResponse('<h1>Error: ' + e + '</h1>')
    else:
        pass

@csrf_exempt 
def predmodel(request, id):
    if request.method == 'POST':
        model = PredictModel.objects.get(id=id)
        request_data = JSONParser().parse(request)
        parameters = request_data['parameters']
        result = str(globals()[model.function_name](parameters)) # execute function with name stored as string in variable.
        print(result[2:-1])
        return JsonResponse({ 'result': result[2:-1] }) 
        # TODO: import new model into database
    else:
        pass