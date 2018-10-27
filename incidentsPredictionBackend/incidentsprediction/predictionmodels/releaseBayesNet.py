import os
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import base64


def releaseBayesNet(evs):
    bayesNet = gum.BayesNet("Quality Prediction")


    # Model's nodes declaration
    numberOfDevelopers = bayesNet.add(gum.LabelizedVariable("Nb Of Developers", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfCommits = bayesNet.add(gum.LabelizedVariable("Nb Of Commits", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfImpactedBranches = bayesNet.add(gum.LabelizedVariable("Nb Of Impacted Branches", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    implementationEffectiveness = bayesNet.add(gum.LabelizedVariable("Implementation Effectiveness", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfFunctionalEvolutions = bayesNet.add(gum.LabelizedVariable("Nb Of Functional Evolutions", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfTechnicalEvolutions = bayesNet.add(gum.LabelizedVariable("Nb Of Technical Evolutions", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    evolution = bayesNet.add(gum.LabelizedVariable("Evolution", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfDefects = bayesNet.add(gum.LabelizedVariable("Nb Of Defects", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    gravityOfDefects = bayesNet.add(gum.LabelizedVariable("Gravity Of Defects", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfFixedDefects = bayesNet.add(gum.LabelizedVariable("Nb Of Fixed Defects", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    testingEffectiveness = bayesNet.add(gum.LabelizedVariable("Testing Effectiveness", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    incident = bayesNet.add(gum.LabelizedVariable("Incident", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    availability = bayesNet.add(gum.LabelizedVariable("Availability", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))


    # Model's links declaration
    for link in [(numberOfDevelopers,implementationEffectiveness), (numberOfCommits,implementationEffectiveness), (numberOfImpactedBranches,implementationEffectiveness), (implementationEffectiveness,incident), (implementationEffectiveness,availability), (numberOfFunctionalEvolutions,evolution), (numberOfTechnicalEvolutions,evolution), (evolution,incident), (numberOfDefects,testingEffectiveness), (gravityOfDefects,testingEffectiveness), (numberOfFixedDefects,testingEffectiveness), (testingEffectiveness,incident), (testingEffectiveness,availability), (incident,availability)]:
        bayesNet.addArc(*link)


    # Model's input nodes' probabilities definition'
    bayesNet.cpt(numberOfDevelopers)[:] = [0.48, 0.36, 0.16]
    bayesNet.cpt(numberOfDevelopers)
    bayesNet.cpt(numberOfCommits)[:] = [0.54, 0.12, 0.34]
    bayesNet.cpt(numberOfCommits)
    bayesNet.cpt(numberOfImpactedBranches)[:] = [0.32, 0.33, 0.35]
    bayesNet.cpt(numberOfImpactedBranches)
    bayesNet.cpt(numberOfFunctionalEvolutions)[:] = [0.38, 0.44, 0.18]
    bayesNet.cpt(numberOfFunctionalEvolutions)
    bayesNet.cpt(numberOfTechnicalEvolutions)[:] = [0.38, 0.44, 0.18]
    bayesNet.cpt(numberOfTechnicalEvolutions)
    bayesNet.cpt(numberOfDefects)[:] = [0.57, 0.15, 0.28]
    bayesNet.cpt(numberOfDefects)
    bayesNet.cpt(gravityOfDefects)[:] = [0.42, 0.21, 0.37]
    bayesNet.cpt(gravityOfDefects)
    bayesNet.cpt(numberOfFixedDefects)[:] = [0.35, 0.28, 0.37]
    bayesNet.cpt(numberOfFixedDefects)


    # Model's connected nodes' probabilities definition'
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Low"}] = 0.01
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Medium"}] = 0.04
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "High"}] = 0.0
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Low"}] = 0.03
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Medium"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "High"}] = 0.03
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Low"}] = 0.02
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Medium"}] = 0.04
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Low", "Nb Of Commits": "High", "Nb Of Impacted Branches": "High"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Low"}] = 0.0
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Medium"}] = 0.04
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "High"}] = 0.03
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Low"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Medium"}] = 0.07
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "High"}] = 0.03
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Low"}] = 0.02
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Medium"}] = 0.05
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "Medium", "Nb Of Commits": "High", "Nb Of Impacted Branches": "High"}] = 0.07
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Low"}] = 0.04
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "Medium"}] = 0.0
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Low", "Nb Of Impacted Branches": "High"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Low"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "Medium"}] = 0.05
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "Medium", "Nb Of Impacted Branches": "High"}] = 0.0
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Low"}] = 0.02
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "High", "Nb Of Impacted Branches": "Medium"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Nb Of Developers": "High", "Nb Of Commits": "High", "Nb Of Impacted Branches": "High"}] = 0.05
    bayesNet.cpt(implementationEffectiveness)
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Low", "Nb Of Technical Evolutions": "Low"}] = 0.19
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Low", "Nb Of Technical Evolutions": "Medium"}] = 0.16
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Low", "Nb Of Technical Evolutions": "High"}] = 0.1
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Medium", "Nb Of Technical Evolutions": "Low"}] = 0.08
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Medium", "Nb Of Technical Evolutions": "Medium"}] = 0.01
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "Medium", "Nb Of Technical Evolutions": "High"}] = 0.03
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "High", "Nb Of Technical Evolutions": "Low"}] = 0.17
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "High", "Nb Of Technical Evolutions": "Medium"}] = 0.17
    bayesNet.cpt(evolution)[{"Nb Of Functional Evolutions": "High", "Nb Of Technical Evolutions": "High"}] = 0.09
    bayesNet.cpt(evolution)
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Low"}] = 0.0
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Medium"}] = 0.07
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "High"}] = 0.01
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Low"}] = 0.02
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Medium"}] = 0.08
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "High"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Low"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Medium"}] = 0.01
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Low", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "High"}] = 0.03
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Low"}] = 0.05
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Medium"}] = 0.03
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "High"}] = 0.03
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Low"}] = 0.08
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Medium"}] = 0.08
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "High"}] = 0.02
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Low"}] = 0.01
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Medium"}] = 0.05
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "Medium", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "High"}] = 0.05
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Low"}] = 0.02
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "Medium"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Low", "Nb Of Fixed Defects": "High"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Low"}] = 0.03
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "Medium"}] = 0.01
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "Medium", "Nb Of Fixed Defects": "High"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Low"}] = 0.07
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "Medium"}] = 0.01
    bayesNet.cpt(testingEffectiveness)[{"Nb Of Defects": "High", "Gravity Of Defects": "High", "Nb Of Fixed Defects": "High"}] = 0.06
    bayesNet.cpt(testingEffectiveness)
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "Low"}] = 0.14
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = 0.86; 0.67
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "High"}] = 0.33; 0.46
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = 0.54; 0.23
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = 0.77; 0.66
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "High"}] = 0.34; 0.09
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "Low"}] = 0.91; 0.58
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "Medium"}] = 0.42; 0.75
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "High"}] = 0.25; 0.64
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "Low"}] = 0.36; 0.19
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = 0.81; 0.72
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "High"}] = 0.28; 0.58
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = 0.42; 0.24
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = 0.76; 0.65
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "High"}] = 0.35; 0.04
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "Low"}] = 0.96; 0.31
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "Medium"}] = 0.69; 0.16
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "High"}] = 0.84; 0.73
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "Low"}] = 0.27; 0.33
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = 0.67; 0.76
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "High"}] = 0.24; 0.35
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = 0.65; 0.44
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = 0.56; 0.92
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "High"}] = 0.08; 0.57
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "Low"}] = 0.43; 0.33
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "Medium"}] = 0.67; 0.51
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "High"}] = 0.49; 0.38
    bayesNet.cpt(incident)


    # Model's output nodes' probabilities definition'
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "Low"}] = ['0.14', '0.86']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = ['0.67', '0.33']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Low", "Testing Effectiveness": "High"}] = ['0.46', '0.54']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = ['0.23', '0.77']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = ['0.66', '0.34']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "Medium", "Testing Effectiveness": "High"}] = ['0.09', '0.91']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "Low"}] = ['0.58', '0.42']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "Medium"}] = ['0.75', '0.25']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Low", "Evolution": "High", "Testing Effectiveness": "High"}] = ['0.64', '0.36']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "Low"}] = ['0.19', '0.81']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = ['0.72', '0.28']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Low", "Testing Effectiveness": "High"}] = ['0.58', '0.42']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = ['0.24', '0.76']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = ['0.65', '0.35']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "Medium", "Testing Effectiveness": "High"}] = ['0.04', '0.96']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "Low"}] = ['0.31', '0.69']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "Medium"}] = ['0.16', '0.84']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "Medium", "Evolution": "High", "Testing Effectiveness": "High"}] = ['0.73', '0.27']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "Low"}] = ['0.33', '0.67']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "Medium"}] = ['0.76', '0.24']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Low", "Testing Effectiveness": "High"}] = ['0.35', '0.65']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "Low"}] = ['0.44', '0.56']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "Medium"}] = ['0.92', '0.08']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "Medium", "Testing Effectiveness": "High"}] = ['0.57', '0.43']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "Low"}] = ['0.33', '0.67']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "Medium"}] = ['0.51', '0.49']
    bayesNet.cpt(incident)[{"Implementation Effectiveness": "High", "Evolution": "High", "Testing Effectiveness": "High"}] = ['0.38', '0.62']
    bayesNet.cpt(incident)
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Incident": "Acceptable"}] = ['0.52', '0.48']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Incident": "Non Acceptable"}] = ['0.17', '0.83']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Incident": "Acceptable"}] = ['0.99', '0.01']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Incident": "Non Acceptable"}] = ['0.12', '0.88']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Incident": "Acceptable"}] = ['0.76', '0.24']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Incident": "Non Acceptable"}] = ['0.9', '0.1']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Incident": "Acceptable"}] = ['0.98', '0.02']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Incident": "Non Acceptable"}] = ['0.51', '0.49']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Incident": "Acceptable"}] = ['0.75', '0.25']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Incident": "Non Acceptable"}] = ['0.4', '0.6']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Incident": "Acceptable"}] = ['0.07', '0.93']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Incident": "Non Acceptable"}] = ['0.43', '0.57']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Incident": "Acceptable"}] = ['0.29', '0.71']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Incident": "Non Acceptable"}] = ['0.18', '0.82']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Incident": "Acceptable"}] = ['0.88', '0.12']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Incident": "Non Acceptable"}] = ['0.88', '0.12']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Incident": "Acceptable"}] = ['0.57', '0.43']
    bayesNet.cpt(availability)[{"Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Incident": "Non Acceptable"}] = ['0.24', '0.76']
    bayesNet.cpt(availability)


    # Evidence definition
    output_parameters_labels = ['Incident', 'Availability']
    ie = gum.LazyPropagation(bayesNet)
    ie.setEvidence(evs)
    print(evs)
    ie.makeInference()
    resultCSV = ['Parameter, Acceptable']
    for output_parameter_label in output_parameters_labels:
        results = ie.posterior(output_parameter_label)
        resultCSV.append(output_parameter_label + ", " + round(results[0],3).__str__())
    return resultCSV