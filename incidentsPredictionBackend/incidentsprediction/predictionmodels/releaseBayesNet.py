from pylab import *
import matplotlib.pyplot as plt
import os
import pyAgrum as gum
import base64
from pyAgrum.lib.bn2graph import BNinference2dot

def releaseBayesNet(evs):

    bayesNet = gum.BayesNet("Quality Prediction")


    # Model's nodes declaration
    requirementsProcessQuality = bayesNet.add(gum.LabelizedVariable("Requirements Process Quality", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    requirementsEffort = bayesNet.add(gum.LabelizedVariable("Requirements Effort", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    requirementsEffectiveness = bayesNet.add(gum.LabelizedVariable("Requirements Effectiveness", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    implementationProcessQuality = bayesNet.add(gum.LabelizedVariable("Implementation Process Quality", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    implementationEffort = bayesNet.add(gum.LabelizedVariable("Implementation Effort", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    implementationEffectiveness = bayesNet.add(gum.LabelizedVariable("Implementation Effectiveness", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    testingProcessQuality = bayesNet.add(gum.LabelizedVariable("Testing Process Quality", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    testingEffort = bayesNet.add(gum.LabelizedVariable("Testing Effort", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    testingEffectiveness = bayesNet.add(gum.LabelizedVariable("Testing Effectiveness", "cloudy ?", 0).addLabel("Low").addLabel("Medium").addLabel("High"))
    efficiency = bayesNet.add(gum.LabelizedVariable("Efficiency", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    satisfaction = bayesNet.add(gum.LabelizedVariable("Satisfaction", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    effectiveness = bayesNet.add(gum.LabelizedVariable("Effectiveness", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    usabilityCompliance = bayesNet.add(gum.LabelizedVariable("Usability Compliance", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    reliabilityCompliance = bayesNet.add(gum.LabelizedVariable("Reliability Compliance", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    availability = bayesNet.add(gum.LabelizedVariable("Availability", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    faultTolerance = bayesNet.add(gum.LabelizedVariable("Fault Tolerance", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    recoverability = bayesNet.add(gum.LabelizedVariable("Recoverability", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    maturity = bayesNet.add(gum.LabelizedVariable("Maturity", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    usability = bayesNet.add(gum.LabelizedVariable("Usability", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))
    reliability = bayesNet.add(gum.LabelizedVariable("Reliability", "cloudy ?", 0).addLabel("Acceptable").addLabel("Non Acceptable"))


    # Model's links declaration
    for link in [(requirementsProcessQuality,requirementsEffectiveness), (requirementsEffort,requirementsEffectiveness), (requirementsEffectiveness,usability), (implementationProcessQuality,implementationEffectiveness), (implementationEffort,implementationEffectiveness), (implementationEffectiveness,usability), (implementationEffectiveness,reliability), (testingProcessQuality,testingEffectiveness), (testingEffort,testingEffectiveness), (testingEffectiveness,usability), (testingEffectiveness,reliability), (usability,reliability), (usability,efficiency), (usability,satisfaction), (usability,effectiveness), (usability,usabilityCompliance), (reliability,reliabilityCompliance), (reliability,availability), (reliability,faultTolerance), (reliability,recoverability), (reliability,maturity)]:
        bayesNet.addArc(*link)


    # Model's input nodes' probabilities definition'
    bayesNet.cpt(requirementsProcessQuality)[:] = [0.48, 0.36, 0.16]
    bayesNet.cpt(requirementsProcessQuality)
    bayesNet.cpt(requirementsEffort)[:] = [0.54, 0.12, 0.34]
    bayesNet.cpt(requirementsEffort)
    bayesNet.cpt(implementationProcessQuality)[:] = [0.32, 0.33, 0.35]
    bayesNet.cpt(implementationProcessQuality)
    bayesNet.cpt(implementationEffort)[:] = [0.38, 0.44, 0.18]
    bayesNet.cpt(implementationEffort)
    bayesNet.cpt(testingProcessQuality)[:] = [0.42, 0.21, 0.37]
    bayesNet.cpt(testingProcessQuality)
    bayesNet.cpt(testingEffort)[:] = [0.57, 0.15, 0.28]
    bayesNet.cpt(testingEffort)


    # Model's connected nodes' probabilities definition'
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Low", "Requirements Effort": "Low"}] = 0.06
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Low", "Requirements Effort": "Medium"}] = 0.01
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Low", "Requirements Effort": "High"}] = 0.2
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Medium", "Requirements Effort": "Low"}] = 0.02
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Medium", "Requirements Effort": "Medium"}] = 0.02
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "Medium", "Requirements Effort": "High"}] = 0.13
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "High", "Requirements Effort": "Low"}] = 0.03
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "High", "Requirements Effort": "Medium"}] = 0.31
    bayesNet.cpt(requirementsEffectiveness)[{"Requirements Process Quality": "High", "Requirements Effort": "High"}] = 0.22
    bayesNet.cpt(requirementsEffectiveness)
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Low", "Implementation Effort": "Low"}] = 0.06
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Low", "Implementation Effort": "Medium"}] = 0.11
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Low", "Implementation Effort": "High"}] = 0.17
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Medium", "Implementation Effort": "Low"}] = 0.03
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Medium", "Implementation Effort": "Medium"}] = 0.08
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "Medium", "Implementation Effort": "High"}] = 0.17
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "High", "Implementation Effort": "Low"}] = 0.17
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "High", "Implementation Effort": "Medium"}] = 0.07
    bayesNet.cpt(implementationEffectiveness)[{"Implementation Process Quality": "High", "Implementation Effort": "High"}] = 0.14
    bayesNet.cpt(implementationEffectiveness)
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Low", "Testing Effort": "Low"}] = 0.04
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Low", "Testing Effort": "Medium"}] = 0.16
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Low", "Testing Effort": "High"}] = 0.13
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Medium", "Testing Effort": "Low"}] = 0.15
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Medium", "Testing Effort": "Medium"}] = 0.1
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "Medium", "Testing Effort": "High"}] = 0.17
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "High", "Testing Effort": "Low"}] = 0.05
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "High", "Testing Effort": "Medium"}] = 0.14
    bayesNet.cpt(testingEffectiveness)[{"Tetsting Process Quality": "High", "Testing Effort": "High"}] = 0.06
    bayesNet.cpt(testingEffectiveness)
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium"}] = 0.08
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High"}] = 0.08
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low"}] = 0
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium"}] = 0.07
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low"}] = 0.03
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium"}] = 0.06
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "High"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low"}] = 0.08
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium"}] = 0
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low"}] = 0.07
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium"}] = 0.04
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High"}] = 0.02
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low"}] = 0.07
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium"}] = 0.06
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "High"}] = 0.03
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High"}] = 0.04
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium"}] = 0.04
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High"}] = 0.07
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low"}] = 0.01
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium"}] = 0.04
    bayesNet.cpt(usability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "High"}] = 0.04
    bayesNet.cpt(usability)
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Low", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "Medium", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Low", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.02
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "Medium", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.04
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Low", "Usability": "Non Acceptable"}] = 0.03
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "Medium", "Usability": "Non Acceptable"}] = 0
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Acceptable"}] = 0.01
    bayesNet.cpt(reliability)[{"Requirements Effectiveness": "High", "Implementation Effectiveness": "High", "Testing Effectiveness": "High", "Usability": "Non Acceptable"}] = 0.01
    bayesNet.cpt(reliability)


    # Model's output nodes' probabilities definition'
    bayesNet.cpt(efficiency)[{"Usability": "Acceptable"}] = ['0.74', '0.26']
    bayesNet.cpt(efficiency)[{"Usability": "Non Acceptable"}] = ['0.35', '0.65']
    bayesNet.cpt(efficiency)
    bayesNet.cpt(satisfaction)[{"Usability": "Acceptable"}] = ['0.33', '0.67']
    bayesNet.cpt(satisfaction)[{"Usability": "Non Acceptable"}] = ['0.68', '0.32']
    bayesNet.cpt(satisfaction)
    bayesNet.cpt(effectiveness)[{"Usability": "Acceptable"}] = ['0.78', '0.22']
    bayesNet.cpt(effectiveness)[{"Usability": "Non Acceptable"}] = ['0.08', '0.92']
    bayesNet.cpt(effectiveness)
    bayesNet.cpt(usabilityCompliance)[{"Usability": "Acceptable"}] = ['0.19', '0.81']
    bayesNet.cpt(usabilityCompliance)[{"Usability": "Non Acceptable"}] = ['0.58', '0.42']
    bayesNet.cpt(usabilityCompliance)
    bayesNet.cpt(reliabilityCompliance)[{"Reliability": "Acceptable"}] = ['0.85', '0.15']
    bayesNet.cpt(reliabilityCompliance)[{"Reliability": "Non Acceptable"}] = ['0.22', '0.78']
    bayesNet.cpt(reliabilityCompliance)
    bayesNet.cpt(availability)[{"Reliability": "Acceptable"}] = ['0.1', '0.9']
    bayesNet.cpt(availability)[{"Reliability": "Non Acceptable"}] = ['0.71', '0.39']
    bayesNet.cpt(availability)
    bayesNet.cpt(faultTolerance)[{"Reliability": "Acceptable"}] = ['0.16', '0.84']
    bayesNet.cpt(faultTolerance)[{"Reliability": "Non Acceptable"}] = ['0.58', '0.42']
    bayesNet.cpt(faultTolerance)
    bayesNet.cpt(recoverability)[{"Reliability": "Acceptable"}] = ['0.41', '0.59']
    bayesNet.cpt(recoverability)[{"Reliability": "Non Acceptable"}] = ['0.70', '0.30']
    bayesNet.cpt(recoverability)
    bayesNet.cpt(maturity)[{"Reliability": "Acceptable"}] = ['0.38', '0.62']
    bayesNet.cpt(maturity)[{"Reliability": "Non Acceptable"}] = ['0.76', '0.24']
    bayesNet.cpt(maturity)


    # Evidence definition
    output_parameters_labels = ['Efficiency', 'Satisfaction', 'Effectiveness', 'Usability Compliance', 'Reliability Compliance', 'Availability', 'Fault Tolerance', 'Recoverability', 'Maturity']
    ie = gum.LazyPropagation(bayesNet)
    ie.setEvidence(evs)
    ie.makeInference()
    resultCSV = []
    resultCSV.append('Parameter, Acceptable, Non-acceptable')
    for output_parameter_label in output_parameters_labels:
        results = ie.posterior(output_parameter_label).tolist()
        resultCSV.append(output_parameter_label + ', ' + str(round(results[0],3)) + ', ' + str(round(results[1], 3)))

    print(resultCSV)
    resultBytes = BNinference2dot(bayesNet, evs=evs, size="20").create(format='png')
    resultBytesStr = base64.b64encode(resultBytes)

    return resultBytesStr, resultCSV