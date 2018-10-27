from django.shortcuts import render
from incidentsprediction.models import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from incidentsprediction.predictionmodels import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def systems_info(request):
    if request.method == 'GET':
        try:
            systems_info = {}
            systems_info['systems'] = []
            qsystems = System.objects.all()
            print(len(qsystems))
            for qsystem in qsystems:
                print(qsystem)
                system_dict = {}
                system_dict['systemofsystem'] = qsystem.systemofsystem.name_systemofsystem
                system_dict['owner'] = qsystem.owner_system.eng_fn + ' ' + qsystem.owner_system.eng_ln
                system_dict['name'] = qsystem.name_system
                system_dict['id'] = qsystem.id_system
                system_dict['type'] = qsystem.type_system
                system_dict['vsystems'] = []
                qvsystems = Vsystem.objects.filter(system=qsystem)
                for qvsystem in qvsystems:
                    vsystem_dict = {}
                    vsystem_dict['system'] = qvsystem.system.name_system
                    vsystem_dict['owner'] = qvsystem.owner_vsystem.eng_fn + ' ' + qvsystem.owner_vsystem.eng_ln
                    vsystem_dict['version'] = qvsystem.version_vsystem
                    vsystem_dict['id'] = qvsystem.id_vsystem
                    system_dict['vsystems'].append(vsystem_dict)
                
                system_dict['appsystems'] = []
                qappsystems = ApplicationSystem.objects.filter(system=qsystem)
                for qappsystem in qappsystems:
                    appsystem_dict = {}
                    system_dict['system'] = qappsystem.system.name_system
                    appsystem_dict['owner'] = qappsystem.owner_applicationsystem.eng_fn + ' ' + qappsystem.owner_applicationsystem.eng_ln
                    appsystem_dict['name'] = qappsystem.name_applicationsystem
                    appsystem_dict['id'] = qappsystem.id_applicationsystem
                    appsystem_dict['vappsystems'] = []
                    qvappsystems = Vapplicationsystem.objects.filter(applicationsystem=qappsystem)
                    for qvappsystem in qvappsystems:
                        vappsystem_dict = {}
                        vappsystem_dict['appsystem'] = qvappsystem.applicationsystem.name_applicationsystem
                        vappsystem_dict['owner'] = qvappsystem.owner_vapplicationsystem.eng_fn + ' ' + qvappsystem.owner_vapplicationsystem.eng_ln
                        vappsystem_dict['version'] = qvappsystem.version_vapplicationsystem
                        vappsystem_dict['id'] = qvappsystem.id_vapplicationsystem
                        appsystem_dict['vappsystems'].append(vappsystem_dict)

                    system_dict['appsystems'].append(appsystem_dict)
                systems_info['systems'].append(system_dict)
            print(len(systems_info['systems']))
            return JsonResponse({ 'systems_info': systems_info })
        except Exception as e:
            return HttpResponse('<h1>Error: ' + str(e) + '</h1>')
    else:
        pass


@csrf_exempt 
def get_inputparameters(request):
    if request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            vsystem = request_data['vsystem']
            vappsystem = request_data['vappsystem']
            qvsystem = Vsystem.objects.get(id_vsystem=vsystem['id'])
            qvappsystem = Vapplicationsystem.objects.get(id_vapplicationsystem=vappsystem['id'])
            qrel_inputparameters = RelInputParameter.objects.filter(vsystem=qvsystem, vapplicationsystem=qvappsystem)
            print('parameters:', len(qrel_inputparameters))
            input_parameters = []
            for qrel_inputparameter in qrel_inputparameters:
                print(qrel_inputparameter)
                print(qrel_inputparameter.inputparameter)
                input_parameter_dict = {}
                input_parameter_dict['name'] = qrel_inputparameter.inputparameter.name
                input_parameter_dict['label'] = qrel_inputparameter.inputparameter.label
                input_parameter_dict['type_value'] = qrel_inputparameter.inputparameter.type_value
                input_parameter_dict['value'] = qrel_inputparameter.value
                input_parameters.append(input_parameter_dict)
            return JsonResponse({ 'input_parameters': input_parameters })
        except Exception as e:
            return HttpResponse('<h1>Error: ' + str(e) + '</h1>')
    else:
        pass


@csrf_exempt 
def call_prediction_model(request):
    if request.method == 'POST':
        model_name = 'releaseBayesNet'
        request_data = JSONParser().parse(request)
        parameters = request_data['parameters']
        print('parameters: ', parameters)
        resultCSV = releaseBayesNet(parameters) # execute function with name stored as string in variable.
        return JsonResponse({ 'resultCSV': resultCSV }) 
    else:
        pass