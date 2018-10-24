import os
import base64
import pyAgrum as gum
from pyAgrum.lib.bn2graph import BNinference2dot

def bayesNet(evs):

    # Creating BayesNet with 4 variables
    bayesNets = gum.BayesNet('Quality Prediction')

    # Adding nodes the long way
    commitNumber = bayesNets.add(gum.LabelizedVariable('Commit Number','cloudy ?',0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfDevloper = bayesNets.add(gum.LabelizedVariable("Number Of Developer", "Devs",0).addLabel("Low").addLabel("Medium").addLabel("High"))
    buildFailures = bayesNets.add(gum.LabelizedVariable('Build Failures','cloudy ?',0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfFixedBug = bayesNets.add(gum.LabelizedVariable('Number Of Fixed Bug','cloudy ?',2))
    nbFunctionalEvolution = bayesNets.add(gum.LabelizedVariable("Number Of Functional Evolution", "Evol",0).addLabel("Low").addLabel("Medium").addLabel("High"))
    categoryOfIncident = bayesNets.add(gum.LabelizedVariable("Incident Category", "Devs",0).addLabel("Tertiaire").addLabel("Secondaire").addLabel("Prmaire"))

    # creation of the links between  nodes 
    for link in [(commitNumber,buildFailures),(numberOfDevloper,buildFailures),(nbFunctionalEvolution,numberOfFixedBug),(buildFailures,numberOfFixedBug),(buildFailures, categoryOfIncident),(numberOfFixedBug,categoryOfIncident )]:
        bayesNets.addArc(*link)
        print(bayesNets)

    bayesNets.cpt(commitNumber)[:]= [0.5,0.3,0.2]
    bayesNets.cpt(numberOfDevloper)[:]= [0.5,0.4,0.5]
    bayesNets.cpt(nbFunctionalEvolution)[:]= [0.5,0.4,0.5]
    print(bayesNets.cpt(numberOfFixedBug).var_names)
    bayesNets.cpt(buildFailures).var_names
    bayesNets.cpt(numberOfDevloper)
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'Number Of Functional Evolution': "Medium"}]=[0.5,0.4]
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'Number Of Functional Evolution': "High"}]=[0.54,0.46]
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'Number Of Functional Evolution': "Low"}]=[0.54,0.46]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'Number Of Functional Evolution': "Medium"}]=[0.5,0.4]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'Number Of Functional Evolution': "High"}]=[0.54,0.46]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'Number Of Functional Evolution': "Low"}]=[0.53,0.47]
    bayesNets.cpt(numberOfFixedBug)

    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Developer': "Low"}] = 0.2
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Developer': "High"}] = 0.4
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Developer': "Low"}] = 0.2
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Developer': "High"}] =  0.9
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Developer': "Medium"}] = 1
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Developer': "Medium"}] =  0.9
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Developer': "Medium"}] = 0.1
    bayesNets.cpt(buildFailures)[{'Commit Number': "Medium", 'Number Of Developer': "Medium"}] = 0.6
    bayesNets.cpt(buildFailures)

    bayesNets.cpt(categoryOfIncident)[{'Build Failures': 0,'Number Of Fixed Bug':0}] = [0.2,0.3,0.5]
    bayesNets.cpt(categoryOfIncident)[{'Build Failures': 0,'Number Of Fixed Bug':1}] = [0.5,0.3,0.2]
    bayesNets.cpt(categoryOfIncident)

    output_parameters_labels = ['Incident Category']
    ie = gum.LazyPropagation(bayesNets)
    ie.setEvidence(evs)
    ie.makeInference()
    resultCSV = []
    resultCSV.append('Parameter, Low, Medium, High')
    for output_parameter_label in output_parameters_labels:
        results = ie.posterior(output_parameter_label).tolist()
        resultCSV.append(output_parameter_label + ', ' + str(round(results[0],3)) + ', ' + str(round(results[1],3)) + ', ' + str(round(results[2],3)))

    #gnb.showInference(bn,evs={})
    resultBytes = BNinference2dot(bayesNets, evs=evs).create(format='png')
    resultBytesStr = base64.b64encode(resultBytes)
    
    return resultBytesStr, resultCSV