import json
from pprint import pprint
from incidentsprediction.models import *
import random


def loadDataFromFile(filePath):
    data = {}
    with open(filePath) as f:
        data = json.load(f)
    return data


def deleteDataInDB():
    for item in RelInputParameter.objects.all():
        item.delete()
    for item in Vsystem.objects.all():
        item.delete()
    for item in Vapplicationsystem.objects.all():
        item.delete()
    for item in ApplicationSystem.objects.all():
        item.delete()
    for item in Vsystemofsystem.objects.all():
        item.delete()
    for item in Systemofsystem.objects.all():
        item.delete()
    for item in InputParameter.objects.all():
        item.delete()
    for item in OutputParameter.objects.all():
        item.delete()
    for item in System.objects.all():
        item.delete()
    for item in Engineer.objects.all():
        item.delete()
    for item in Value.objects.all():
        item.delete()
    for item in Parameter.objects.all():
        item.delete()
    for item in PredictModel.objects.all():
        item.delete()


def importModelsInfo(models):
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


def importSystemsInfo(systems_info):
    for item in systems_info['engineers']:
        new_eng = Engineer(eng_fn=item['eng_fn'], eng_ln=item['eng_ln'], company=item['company'], departement=item['departement'], function=item['function'] )
        new_eng.save()

    for item in systems_info['systemofsystems']:
        eng_fn, eng_ln = item['owner'].split(' ')
        owner = Engineer.objects.get(eng_ln=eng_ln, eng_fn=eng_fn)
        new_sysofsys = Systemofsystem(name_systemofsystem=item['name'], owner_systemofsystem=owner)
        new_sysofsys.save()

    for item in systems_info['systems']:
        eng_fn, eng_ln = item['owner'].split(' ')
        owner = Engineer.objects.get(eng_ln=eng_ln, eng_fn=eng_fn)
        sysofsys = Systemofsystem.objects.get(name_systemofsystem=item['systemofsystem'])
        new_sys = System(name_system=item['name'], owner_system=owner, type_system=item['type'], systemofsystem=sysofsys)
        new_sys.save()

    for item in systems_info['applicationsystems']:
        eng_fn, eng_ln = item['owner'].split(' ')
        owner = Engineer.objects.get(eng_ln=eng_ln, eng_fn=eng_fn)
        system = System.objects.get(name_system=item['system'])
        new_appsys = ApplicationSystem(name_applicationsystem=item['name'], owner_applicationsystem=owner, system=system)
        new_appsys.save()

    for item in systems_info['inputparameters']:
        new_inputparam = InputParameter(name=item['name'], label=item['label'], type_value=item['type_value'])
        new_inputparam.save()

    for item in systems_info['outputparameters']:
        new_outputparam = OutputParameter(name=item['name'], label=item['label'], type_value=item['type_value'])
        new_outputparam.save()

    for system in System.objects.all():
        for i in range(3):
            owner = Engineer.objects.all()[0]
            new_vsystem = Vsystem(version_vsystem=i, owner_vsystem=owner,system=system)
            new_vsystem.save()

    for sysofsys in Systemofsystem.objects.all():
        for i in range(3):
            owner = Engineer.objects.all()[0]
            new_vsysofsys = Vsystemofsystem(systemofsystem=sysofsys, name_vsystemofsystem=i, owner_vsystemofsystem=owner)
            new_vsysofsys.save()

    for appsys in ApplicationSystem.objects.all():
        for i in range(3):
            owner = Engineer.objects.all()[0]
            new_vappsys = Vapplicationsystem(version_vapplicationsystem=i, applicationsystem=appsys, owner_vapplicationsystem=owner)
            new_vappsys.save()

    array_values = ["Low", "Medium", "High"]
    for vsystem in Vsystem.objects.all():
        for vapplicationsystem in Vapplicationsystem.objects.all():
            input_params = InputParameter.objects.all()
            for input_param in input_params:
                new_relinputparameter = RelInputParameter(vsystem=vsystem, vapplicationsystem=vapplicationsystem, inputparameter=input_param, value=array_values[random.randint(0, 2)])
                new_relinputparameter.save()


models_info = loadDataFromFile('modelsInfo.json')['modelsInfo']
systems_info = loadDataFromFile('systemsInfo.json')['systemsInfo']

deleteDataInDB() # Remove existing data in the DB
importModelsInfo(models_info) ## Import models into the DB
importSystemsInfo(systems_info) # Import SI into the DB