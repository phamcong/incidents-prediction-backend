import json
from pprint import pprint
from incidentsprediction.models import *

def loadModelsData(filePath):
    models_data = {}
    with open(filePath) as f:
        models_data = json.load(f)['models']
    return models_data


def modelsImport(models):
    for model in models:
        new_model = PredictModel(name=model['name'], label=model['label'], function_name=model['function_name'])
        new_model.save()
        for parameter in model['parameters']:
            new_parameter = Parameter(name=parameter['name'], label=parameter['label'])
            new_parameter.save()

            values = parameter['values']
            for value in values:
                qvalues = Value.objects.filter(type_value=parameter['type_value'], value=str(value))
                if len(qvalues) > 0:
                    new_parameter.values.add(qvalues[0])
                else:
                    new_value = Value(type_value=parameter['type_value'], value=str(value))
                    new_value.save()
                    new_parameter.values.add(new_value)
            new_model.parameters.add(new_parameter)


models_data = loadModelsData('modelsData.json')
modelsImport(models_data)